// Set header content
const fundName = getMapInfo('fund_map', thisFundArray[0], 'title');
const legalName = getMapInfo('fund_map', thisFundArray[0], 'legalName');
const fundType = getMapInfo('fund_map', thisFundArray[0], 'type');

$('.fund-header__icon img').attr('src', `assets/images/fund-icon--${thisFundArray[0].toLowerCase()}.svg`).fadeIn(50);
$('.fund-header__ticker').text(thisFundArray[0]);
if (legalName) {
  $('.fund-header__name').html(legalName);
} else {
  $('.fund-header__name').text(fundName);
}

// Show appropriate navchange arrow
function dailyPriceComplete(data) {
  if (data[0].navchange > 0) {
    $('.pricing-arrow.up').show();
  } else if (data[0].navchange < 0) {
    $('.pricing-arrow.down').show();
  }
}

// Adjust subnav to work on holdings page
const pathname = window.location.pathname;

if (pathname.includes('holdings')) {
  $('.subnav__link').each(function() {
    const href = $(this).attr('href');
    const fundUrl = '../' + thisFundArray[0].toLowerCase();

    $(this).attr('href', fundUrl + href);
  });

  $('.subnav__item').removeClass('active');
  $('.subnav__holdings').addClass('active');
}

// Holdings subnav button directs to waypoint so header is collapsed on load
const waypointUrl = '../holdings/' + thisFundArray[0].toLowerCase() + '#holdings';
$('.subnav__holdings').find('a').attr('href', waypointUrl);

// Remove Distributions and add ETP Document Library to subnav - ETPs only
if (fundType === 'ETP') {
  $('.subnav__distributions').hide()
  $('.subnav__etp').show();
}

// Show Attribution PDF link on USG
if (thisFundArray[0] === 'USG') {
  $('.subnav__attribution').show();
}

// Build mobile subnav dropdown options
function buildFundDropdown() {
  const ticker = thisFundArray[0].toLowerCase();
  let dropdownOptions = '';

  if (pathname.includes('holdings')) {
    $('.styledSelectMobile').html('Holdings')
    dropdownOptions += `<li><a href="../${ticker}#overview">Overview</a></li>`;
    dropdownOptions += `<li><a href="../${ticker}#keyFacts">Key Facts</a></li>`;
    dropdownOptions += `<li rel="#holdings" role="option" tabindex="0">Holdings</li>`;
    dropdownOptions += `<li><a href="../${ticker}#performance">Performance</a></li>`;

    if (fundType === 'ETF') {
      dropdownOptions += `<li><a href="../${ticker}#distributions">Distributions</a></li>`;
    }
  } else {
    dropdownOptions += `<li rel="#overview" role="option" tabindex="0">Overview</li>`;
    dropdownOptions += `<li rel="#keyFacts" role="option" tabindex="0">Key Facts</li>`;
    dropdownOptions += `<li><a href="../holdings/${ticker}">Holdings</a></li>`;
    dropdownOptions += `<li rel="#performance" role="option" tabindex="0">Performance</li>`;

    if (fundType === 'ETF') {
      dropdownOptions += `<li rel="#distributions" role="option" tabindex="0">Distributions</li>`;
    }
  }
  
  dropdownOptions += `<li><a href="../resources">Resources</a></li>`;
  if (fundType === 'ETP') {
    dropdownOptions += `<li><a href="../resources/${ticker}">ETP Document Library</a></li>`;
  }

  $('#hiddenFundDropdown').html(dropdownOptions);
}

buildFundDropdown();

// morningstar rating

const morningstarObj = {
  SDCI: {
    rating: 5,
    groupOverall: 99,
    fundCategory: 'Commodities Broad Basket',
    historical: {
      rating3yr: 5,
      group3yr: 98,
      rating5yr: 5,
      group5yr: 92,
    }
  },
  USCI: {
    rating: 5,
    groupOverall: 99,
    fundCategory: 'Commodities Broad Basket',
    historical: {
      rating3yr: 5,
      group3yr: 98,
      rating5yr: 5,
      group5yr: 92,
      rating10yr: 3,
      group10yr: 66,
    }
  },
  UMI: {
    rating: 4,
    groupOverall: 91,
    fundCategory: 'Energy Limited Partnership',
    historical: {
      rating3yr: 4,
      group3yr: 91,
    }
  }
};

if (morningstarObj.hasOwnProperty(thisFundArray[0])) {
  const asOfDate = '6/30/2026';

  const morningstar = morningstarObj[thisFundArray[0]];
  
  const tooltipText = `Overall rating out of ${morningstar.groupOverall} ${morningstar.fundCategory} funds as of ${asOfDate} based on risk adjusted returns.`;

  let footerDisclosureA = `The ${fundName} was rated against the following numbers of ${morningstar.fundCategory} funds over the following time periods: ${morningstar.historical.group3yr} funds in the last three years`;

  let footerDisclosureB = `With respect to these ${morningstar.fundCategory} funds, the ${fundName} received a Morningstar Rating of ${morningstar.historical.rating3yr} stars`;

  if (morningstar.historical.hasOwnProperty('rating10yr')) {
    footerDisclosureA += `, ${morningstar.historical.group5yr} funds in the last five years and ${morningstar.historical.group10yr} funds for the last ten years for the period ending ${asOfDate}.`;
    footerDisclosureB += `, ${morningstar.historical.rating5yr} stars and ${morningstar.historical.rating10yr} stars for the three, five, and ten-year periods, respectively.`;

  } else if (morningstar.historical.hasOwnProperty('rating5yr')) {
    footerDisclosureA += ` and ${morningstar.historical.group5yr} funds in the last five years for the period ending ${asOfDate}.`;
    footerDisclosureB += `, and ${morningstar.historical.rating5yr} stars for the three, and five-year periods, respectively.`;

  } else {
    footerDisclosureA += ` for the period ending ${asOfDate}.`;
    footerDisclosureB += ` for the three-year period.`;
  }

  $('#morningstarStars').html('&starf;'.repeat(morningstar.rating));
  $('#morningstar-label').text(tooltipText);
  $('#morningstar-footer').text(`${footerDisclosureA} ${footerDisclosureB}`);
}

// add guide buttons to fund-header__docs

let needGuideButton = false;
let needHandoutButton = false;
let buttonTag;

if (thisFundArray[0] === 'SDCI') {

  needGuideButton = true;
  buttonTag = 'commodity';

} else if (thisFundArray[0] === 'UMI') {

  needGuideButton = true;
  needHandoutButton = true;
  buttonTag = 'energy';

} else if (thisFundArray[0] === 'ZSB') {

  needGuideButton = true;
  buttonTag = 'electrification';

} else if (thisFundArray[0] === "WTIB") {

  needGuideButton = true;
  buttonTag = 'exposure';

}

if (needGuideButton) {
  const guideButton = `
    <a class="button" href="" data-location="domain" data-type="edu" data-key="documentname" data-tag="${buttonTag}"><span data-key="title"></span></a>
  `;

  $('.fund-header__docs').append(guideButton);
}

if (needHandoutButton) {
  const handoutButton = `
    <a class="button" href="" data-location="domain" data-type="hand" data-key="documentname" data-tag="${buttonTag}"><span data-key="title"></span></a>
  `;

  $('.fund-header__docs').append(handoutButton);
}