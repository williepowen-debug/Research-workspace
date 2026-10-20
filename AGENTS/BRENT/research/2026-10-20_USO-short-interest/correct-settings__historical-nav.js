function getHistoricalNav(ticker) {
  return new Promise((resolve, reject) => {
    const apiRequest = api_url_v2 + 'historicalnav/' + ticker + '/inception-today';
    const dataCacheRecord = 'historicalnav_' + ticker + '_si';

    api.getData(apiRequest, dataCacheRecord, function (data) {
      if (verifyData(data)) {
        $('#downloadHistorical').removeClass('cursor-wait');
        resolve(data[0][ticker]);
      } else {
        reject(`Unable to verify API response for ${ticker} Historical NAV`);
      }
    });
  });
}

const buildHistoricalNavFile = (ticker, data) => {
  const endDate = data[data.length - 1].date;

  // example: usci-historicalnav-20250715.csv
  const filename = `${ticker.toLowerCase()}-historicalnav-${dayjs(endDate).format('YYYYMMDD')}.csv`;

  let csv = ticker + ' Historical NAV Performance\n';
  csv += 'Date,NAV Value\n';

  $.each(data, function (i, val) {
    csv += dateFormatter_v3(val.date) + ',';
    csv += val.value.toLocaleString('en-US', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
      style: 'currency',
      currency: 'USD',
    });
    csv += '\n';
  });

  download_csv(csv, filename);
};

const download_csv = (csv, filename) => {
  let csvFile;
  let downloadLink;

  // CSV FILE
  csvFile = new Blob([csv], { type: 'text/csv;charset=utf-8' });

  // Download link
  downloadLink = document.createElement('a');

  // File name
  downloadLink.download = filename;

  if (window.navigator.msSaveOrOpenBlob && window.Blob) {
    navigator.msSaveOrOpenBlob(csvFile, 'strings.csv');
  }

  // We have to create a link to the file
  downloadLink.href = window.URL.createObjectURL(csvFile);

  // Make sure that the link is not displayed
  downloadLink.style.display = 'none';

  // Add the link to your DOM
  document.body.appendChild(downloadLink);

  // Lanzamos
  downloadLink.click();
};

async function initHistoricalNav() {
  try {
    const historicalNav = await getHistoricalNav(thisFundArray[0]);

    $('#downloadHistorical').click(() => {
      buildHistoricalNavFile(thisFundArray[0], historicalNav);
    });
  } catch (err) {
    $('#downloadHistorical').hide();
    $('#downloadHistoricalFallback').show();
    console.error(err);
  }
}

initHistoricalNav();