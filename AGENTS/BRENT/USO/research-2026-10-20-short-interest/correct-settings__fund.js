const settingsFundType = getMapInfo('fund_map', thisFundArray[0], 'type');

// dailyprice
$(document).ready(function () {
  dailyprice.run();
  expense.run();
});

if (settingsFundType === 'ETF') {
  median_30_day.run();
  distributionyield.run();

  // Hide yields that do not have a current value
  function yieldComplete(data,settings) {
    if (data.length === 0) {
      const dataPeriod = settings.yieldperiod;
      $(`[data-yieldperiod="${dataPeriod}"]`).closest('tr').hide();
    }
  }
}

if (thisFundArray[0] === 'USO') {
  $('#keyFactsNavHeader').append('<sup>^</sup>');
  $('.premiumBasisPoints + .disclosure').append('<p>The amount of the discount or premium in the trading price of USO relative to USO’s NAV per share may be influenced by various factors including, among other things, the number of investors who seek to purchase or sell shares in the secondary market, availability of Creation Baskets, the liquidity of the oil futures, and the market for Other Oil-Related Investments.</p>');
  initRolling30Day();
}

if (thisFundArray[0] === 'UNG') {
  $('#keyFactsNavHeader').append('<sup>^</sup>');
}

// performance
getAllPerformance(thisFundArray);

// distributions
if (settingsFundType === 'ETF') {
  if (thisFundArray[0] !== "WTIB") {
    callFor_Distributions(thisFundArray);
  }

  switch (thisFundArray[0]) {
    case 'SDCI':
    case 'UDI':
      $('.s19').hide();
      $('.f8937').hide();
      $('.distributions-table').css('min-width', '865px');
        break;
    case 'UMI':
      $('.distributions-table').css('min-width', '1115px');
      break;
    default:
      $('.distributions-table').css('min-width', '985px');
  }
}

if (thisFundArray[0] === 'UMI') {
  function distributionsDataComplete(data) {
    console.log('Adding Updated Form 8937 for UMI');

    const table = document.getElementById('table__distributions');
    const numRows = table.rows.length;

    // add header for Updated Form 8937
    $('#table__distributions tr:nth-child(1)').append('<th>Updated Form 8937</th>');

    // loop through distribution dates and add updated form to appropriate dates
    for (let r = 1; r < numRows; r++) {
      let paydate = table.rows[r].cells.item(2).innerHTML;
      let target = r + 1;
      let updateTag = '';

      switch (paydate) {
        case '11/30/2021':
        case '09/17/2021':
        case '06/30/2021':
          updateTag = '021422update';
          break;
        case '12/30/2022':
          updateTag = '121123update';
      }

      if (updateTag === '') {
        $('#table__distributions tr:nth-child(' + target + ')').append('<td></td>');
      } else {
        let updatedDocCell = `<td class='f8937' data-location='UMI' data-type='8937' data-tag='${updateTag}' data-id='update-${r}'><a href='' data-key='documentname' target='_blank'><img src='assets/images/document-download.svg' alt='Download Updated Form 8937' width='16' height='21'></a></td>`;
        $('#table__distributions tr:nth-child(' + target + ')').append(updatedDocCell);
      }
    }
    collect_document_elements();
  }
}

function docDataComplete(html_data, api_data) {
  const fundsWithRelatedInsights = ['SDCI', 'UMI', 'USE', 'USG', 'ZSB'];
  let count = 0;

  if (fundsWithRelatedInsights.includes(thisFundArray[0])) {
    // Update blog "Related Insights" to link to their individual pages
    $('.section__related-insights').each(function() {
      const loopLength = 4; // # of posts to display 
      const docType = $(this).data('abbrev');
      const docTag = $(this).data('tag');
      const tagContainsFundTicker = docTag?.includes(thisFundArray[0].toLowerCase());

      if (tagContainsFundTicker && docType === 'MU') {
        $('.section__related-insights-wrapper').show();
        $(this).show();
        
        docURL = $(this).data('url')
          .replace('.pdf', '')
          .replace('documents/', 'blog/');

        $(this).find('a').attr({
          'target': '_self',
          'href': `../${docURL}`
        });

        count++;

        if (count > loopLength - 1) return false;
      }
    });
  }
}