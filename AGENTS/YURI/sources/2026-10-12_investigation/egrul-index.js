function i18n(s) {
    return s;
}
var RES_PAGE_SIZE = 20;

$(function () {
    window.setTimeout(function() {
        $("#uniPageHeader > .page-title").unbind("click");
    }, 100);
    $("#resultContent").on("click", ".op-excerpt", function () {
        checkCaptchaAndRequestVyp($(this).data("t"));
        return false;
    });
    $(".query-field-clear,.query-field-caption").click(function () {
        $("#query").val("");
        $("#resultPanel").hide();
        return false;
    });
    $("#btnReference").click(function() {
        checkCaptchaAndRequestVyp($(this).data("t"));
        return false;
    });
    $("#btnSearch").click(function() {
        $("#pageField").val("");
    });
});

function frmSearch_onsubmit(form) {
    return checkCaptchaAndSubmit(form);
}

function checkCaptchaAndSubmit(form) {
    if (isCaptchaRequired() && !isCaptchaReady()) {
        showCaptchaDialog(function(captchaToken) {
            $('input[name="vyp3CaptchaToken"]').val(captchaToken);
            $("#resultPanel").hide();
            $(form).submit();
        });
        return false;
    }
    resetCaptcha();
    return true;
}

function form_onsuccess (result) {
    blockUI();
    window['CAPTCHA_REQUIRED'] = result['captchaRequired'];
    waitForResult(result.t);
    return true;
}

function form_errors(errors) {
    $("#resultPanel").hide();
    if (errors['captchaSearch']) {
        window['CAPTCHA_REQUIRED'] = true;
        $('#frmSearch').submit();
    } else if (errors['captchaVyp']) {
        window['CAPTCHA_REQUIRED'] = true;
        checkCaptchaAndRequestVyp(errors['t'][0]);
    } else {
        window.setTimeout(function() {
            showErrors(errors);
        }, 100);
    }
}

function waitForResult (t) {
    $.ajax({
        url: "search-result/" + t + "?r=" + (new Date()).getTime(),
        cache: false,
        type: "GET",
        success: function (data) {
            if (!processResult(data)) {
                setTimeout(function () {
                    waitForResult(t)
                }, 1000);
            }
        }
    });
}

function processResult (result) {
    if (result.status == "wait") {
        return false;
    }
    var ht;
    var rows = result.rows;
    var cnt = 0;
    var tot = 0;
    var spravT = false;
    var curPage = 0;
    var numPages = 0;
    if (rows && rows.length > 0) {
        cnt = +rows[0].cnt;
        tot = +rows[0].tot;
        curPage = +rows[0].pg;
        numPages = Math.floor(cnt / RES_PAGE_SIZE) + (((cnt % RES_PAGE_SIZE) > 0) ? 1 : 0);
        if (cnt <= 0 || rows[rows.length - 1].cnt === '0') {
            spravT = rows[rows.length - 1].t;
            rows.pop();
        }
    }
    if (cnt > 0) {
        $("#noDataFound").hide();
        ht = getResultHtml(rows, curPage);
    } else {
        $("#noDataFound").show();
        ht = "";
    }
    $('#resultContent').html(ht).toggle(cnt > 0);
    $("#totTxt").text(tot);
    $("#cntTxt").text(cnt);
    $("#tooManyRows").toggle(tot > cnt);
    $("#vypInfo").toggle(cnt > 0);
    $('#btnReference').data('t', spravT);
    $('#referenceButtonPanel').toggle(!!spravT);
    $("#resultPanel").show();
    showResultPager(numPages, curPage);
    unblockUI(function() {
        scrollToElement($("#resultPanel"));
    });
    return true;
}

function showResultPager(numPages, curPage) {
    var $resultPager = $("#resultPanel .result-pager");
    if (numPages <= 1) {
        $resultPager.hide();
        return;
    }
    var ht = getPagerHtml(getPagerButtons(numPages, curPage), curPage);
    $resultPager.html(ht).show();
    $resultPager.off("click", ".lnk-page");
    $resultPager.on("click", ".lnk-page", function (event) {
        var page = $(this).data("page");
        var curPage = $(".lnk-page-active").data("page");
        if (page == "prev") {
            page = curPage - 1;
        } else if (page == "next") {
            page = curPage + 1;
        }
        if (page < 1 || page > numPages || page == curPage) {
            return false;
        }
        event.stopImmediatePropagation();
        $("#pageField").val(page);
        $("#frmSearch").submit();
        return false;
    });
}

function getPagerButtons(numPages, curPage) {
    var buttons = [1, 2, 3, 4, 5, 6, 7, 8, Math.max(numPages, 11) - 2, Math.max(numPages, 11) - 1, Math.max(numPages, 11)];
    if (numPages <= buttons.length) {
        return buttons.slice(0, numPages);
    }
    if (curPage >= 7) {
        buttons[2] = 0;
    }
    if (curPage <= numPages - 6) {
        buttons[8] = 0;
    }
    var offset = curPage - 5;
    if (curPage <= 6) {
        offset = 1;
    } else if (curPage >= numPages - 5) {
        offset = numPages - 10;
    }
    for (var i = 3; i <= 7; i++) {
        buttons[i] = i + offset;
    }
    return buttons;
}

function getPagerHtml(buttons, curPage) {
    var ht = [];
    ht.push("<ul class='page-nav'><li><a href='#' class='lnk-page lnk-page-prev' data-page='prev'>&nbsp;</a></li>");
    for (var i = 0; i < buttons.length; i++) {
        if (buttons[i] == 0) {
            ht.push("<li>...</li>");
        } else {
            ht.push("<li><a href='#' class='lnk-page lnk-page" + buttons[i] + ((buttons[i] == curPage) ? " lnk-page-active" : "") + "' data-page='" + buttons[i] + "'>" + buttons[i] + "</a></li>");
        }
    }
    ht.push("<li><a href='#' class='lnk-page lnk-page-next' data-page='next'>&nbsp;</a></li></ul>");
    ht.push('<div class="clear"></div>');
    return ht.join("");
}

function getResultHtml(rows, curPage) {
    var meta = {
        'ul': {
            fields: ['rn', 'o', 'r', 'i', 'p', 'g', 'e', 'v', 'orn', 'onz', 'oknp'],
            capts: ['', 'ОГРН', 'Дата присвоения ОГРН', 'ИНН', 'КПП', '', 'Дата прекращения деятельности', 'Дата признания регистрации недействительной',
                'Сведения о номерах юридического лица на день принятия в Российскую Федерацию', '', '']
        },
        'ul1': {
            fields: ['rn', 'o', 'r', 'i', 'p', 'g', 'e', 'v', 'orn', 'oknp'],
            capts: ['', 'ОГРН', 'Дата присвоения ОГРН', 'ИНН', 'КПП', '', 'Дата прекращения деятельности', 'Дата признания регистрации недействительной',
                'Сведения о номерах юридического лица на день принятия в Российскую Федерацию: регистрационный номер', 'идентификационный код юридического лица']
        },
        'fl': {
            fields: ['o', 'i', 'r', 'e', 'v'],
            capts: ['ОГРНИП', 'ИНН', 'Дата присвоения ОГРНИП', 'Дата прекращения деятельности', 'Дата признания регистрации недействительной']
        }
    };
    var ht = [];
    for (var i = 0; i < rows.length; i++) {
        var row = rows[i];
        var kind = row['k'];
        if (kind == 'ul'){
            var o184 = (row['o184'] == '1');
            if (o184) {
                kind = 'ul1';
            }
        }
        ht.push('<div class="res-row">');
        ht.push('<div class="res-rownum">' + (1 + i + (curPage - 1) * RES_PAGE_SIZE) + '.</div>');
        var title = htmlEncode(row['c']) || i18n((row['k'] == 'ul') ? 'Сокращенное наименование отсутствует' :'Получить выписку');
        ht.push('<div class="res-caption"><a href="#" class="op-excerpt" data-t="' + row["t"] + '" title="' + title + '">' + row["n"] + '</a></div>');
        ht.push('<div class="res-line">');
        ht.push('<div class="res-text">');
        var capts = meta[kind].capts;
        var fields = meta[kind].fields;
        var spanOpen = false;
        for (var j in fields) {
            var val = row[fields[j]];
            if (!val) {
                continue;
            }
            if (spanOpen) {
                ht.push(', ');
            }
            if (capts[j]) {
                ht.push(capts[j]);
                ht.push(':&nbsp;');
            }
            ht.push(htmlEncode(val));
            spanOpen = true;
        }
        ht.push('</div>');
        ht.push('<button class="btn-with-icon btn-excerpt op-excerpt" data-t="' + row["t"] + '">' + 'Получить выписку' + '</button>');
        ht.push('</div>');
        ht.push('</div>');
    }
    return ht.join("");
}

function checkCaptchaAndRequestVyp(t) {
    if (isCaptchaRequired() && !isCaptchaReady()) {
        showCaptchaDialog(function(captchaToken) {
            $('input[name="vyp3CaptchaToken"]').val(captchaToken);
            resetCaptcha();
            requestVyp(t);
        });
        return false;
    }
    resetCaptcha();
    requestVyp(t);
    return true;
}

function requestVyp (t) {
    blockUI();
    $.ajax({
        url: "vyp-request/" + t + "?r=" + $('input[name="vyp3CaptchaToken"]').val(),
        cache: false,
        type: "GET",
        success: function (data) {
            window['CAPTCHA_REQUIRED'] = data['captchaRequired'];
            waitForVyp(t);
        }
    });
}

function waitForVyp (t) {
    $.ajax({
        url: "vyp-status/" + t + "?r=" + (new Date()).getTime(),
        cache: false,
        type: "GET",
        success: function (data) {
            if (data.status == "ready") {
                unblockUI();
                window.location = "vyp-download/" + t;
            } else if (data.status == "error") {
                unblockUI();
                showUniAlert("Истёк срок действия ссылки. Пожалуйста, повторите поиск.");
            } else {
                setTimeout(function () {
                    waitForVyp(t)
                }, 1000);
            }
        }
    });
}

function scrollToElement($el) {
    window.setTimeout(function() {
        $('html, body').animate({
            scrollTop: $($el).offset().top
        });
    }, 100);
}
