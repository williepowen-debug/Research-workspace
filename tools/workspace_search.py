#!/usr/bin/env python3
"""
Semantic search over workspace markdown files.

Usage:
    python workspace_search.py index     # Index all .md files
    python workspace_search.py "query"   # Search
    python workspace_search.py status    # Show index stats
"""

import sys
import hashlib
import re
from pathlib import Path
from typing import Generator

# Lazy imports for faster CLI response
def get_model():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer('all-MiniLM-L6-v2')

def get_collection():
    import chromadb
    client = chromadb.PersistentClient(path=str(DB_PATH))
    return client.get_or_create_collection(
        name="workspace",
        metadata={"hnsw:space": "cosine"}
    )

# Paths
WORKSPACE = Path.home() / ".openclaw/workspace"
DB_PATH = WORKSPACE / ".search_index"
EXCLUDE_DIRS = {".git", "node_modules", ".search_index", ".venv", "__pycache__", "media"}
EXCLUDE_FILES = {"package-lock.json", "yarn.lock"}

def chunk_markdown(text: str, filepath: str, max_tokens: int = 400) -> Generator[dict, None, None]:
    """
    Split markdown by headings, keeping chunks under max_tokens.
    Yields dicts with: id, text, heading, file
    """
    # Split by headings
    sections = re.split(r'^(#{1,4}\s+.+)$', text, flags=re.MULTILINE)
    
    current_heading = filepath
    current_text = ""
    chunk_idx = 0
    
    for i, section in enumerate(sections):
        if re.match(r'^#{1,4}\s+', section):
            # This is a heading
            if current_text.strip():
                # Yield previous chunk
                chunk_id = hashlib.md5(f"{filepath}:{chunk_idx}".encode()).hexdigest()
                yield {
                    "id": chunk_id,
                    "text": f"# {current_heading}\n\n{current_text.strip()}",
                    "heading": current_heading,
                    "file": filepath
                }
                chunk_idx += 1
            current_heading = section.strip().lstrip('#').strip()
            current_text = ""
        else:
            current_text += section
    
    # Don't forget last chunk
    if current_text.strip():
        chunk_id = hashlib.md5(f"{filepath}:{chunk_idx}".encode()).hexdigest()
        yield {
            "id": chunk_id,
            "text": f"# {current_heading}\n\n{current_text.strip()}",
            "heading": current_heading,
            "file": filepath
        }

def find_markdown_files() -> Generator[Path, None, None]:
    """Find all .md files in workspace, excluding certain dirs."""
    for md in WORKSPACE.rglob("*.md"):
        if any(excl in md.parts for excl in EXCLUDE_DIRS):
            continue
        if md.name in EXCLUDE_FILES:
            continue
        yield md

def index_workspace():
    """Index all markdown files."""
    print("🔍 Loading model...")
    model = get_model()
    collection = get_collection()
    
    # Clear existing
    print("🗑️  Clearing old index...")
    try:
        collection.delete(where={"file": {"$ne": ""}})
    except:
        pass  # Collection might be empty
    
    print("📂 Finding markdown files...")
    files = list(find_markdown_files())
    print(f"   Found {len(files)} files")
    
    total_chunks = 0
    for i, filepath in enumerate(files):
        try:
            text = filepath.read_text(encoding='utf-8', errors='ignore')
            rel_path = str(filepath.relative_to(WORKSPACE))
            
            chunks = list(chunk_markdown(text, rel_path))
            if not chunks:
                continue
                
            # Embed all chunks for this file
            texts = [c["text"] for c in chunks]
            embeddings = model.encode(texts, show_progress_bar=False)
            
            # Upsert to collection
            collection.upsert(
                ids=[c["id"] for c in chunks],
                embeddings=embeddings.tolist(),
                documents=texts,
                metadatas=[{"file": c["file"], "heading": c["heading"]} for c in chunks]
            )
            
            total_chunks += len(chunks)
            print(f"   [{i+1}/{len(files)}] {rel_path}: {len(chunks)} chunks")
            
        except Exception as e:
            print(f"   ⚠️  Error processing {filepath}: {e}")
    
    print(f"\n✅ Indexed {total_chunks} chunks from {len(files)} files")
    print(f"📁 Index stored at: {DB_PATH}")

def search(query: str, k: int = 5):
    """Search the index."""
    model = get_model()
    collection = get_collection()
    
    # Check if index exists
    if collection.count() == 0:
        print("⚠️  Index is empty. Run 'python workspace_search.py index' first.")
        return
    
    # Embed query
    query_embedding = model.encode(query).tolist()
    
    # Search
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        include=["documents", "metadatas", "distances"]
    )
    
    print(f"\n🔍 Results for: \"{query}\"\n")
    print("=" * 60)
    
    for i, (doc, meta, dist) in enumerate(zip(
        results["documents"][0],
        results["metadatas"][0], 
        results["distances"][0]
    )):
        score = 1 - dist  # Convert distance to similarity
        print(f"\n📄 [{i+1}] {meta['file']}")
        print(f"   Section: {meta['heading']}")
        print(f"   Score: {score:.3f}")
        print(f"   ---")
        # Show first 400 chars
        preview = doc[:400].replace('\n', '\n   ')
        print(f"   {preview}...")
        print()

def status():
    """Show index status."""
    import chromadb
    
    if not DB_PATH.exists():
        print("❌ No index found. Run 'python workspace_search.py index' first.")
        return
        
    client = chromadb.PersistentClient(path=str(DB_PATH))
    collection = client.get_or_create_collection("workspace")
    
    count = collection.count()
    size_mb = sum(f.stat().st_size for f in DB_PATH.rglob("*") if f.is_file()) / 1024 / 1024
    
    print(f"📊 Index Status")
    print(f"   Chunks indexed: {count}")
    print(f"   Index size: {size_mb:.1f} MB")
    print(f"   Location: {DB_PATH}")

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    cmd = sys.argv[1]
    
    if cmd == "index":
        index_workspace()
    elif cmd == "status":
        status()
    else:
        # Treat as search query
        query = " ".join(sys.argv[1:])
        search(query)

if __name__ == "__main__":
    main()
