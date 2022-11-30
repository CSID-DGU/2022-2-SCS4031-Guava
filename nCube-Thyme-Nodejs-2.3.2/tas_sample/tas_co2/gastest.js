var mcpadc = require('mcp-spi-adc');

var gassensor = mcpadc.openMcp3008(0, {speedHz: 1350000}, err => {
  if (err) throw err;

  setInterval(_ => {
    gassensor.read((err, reading) => {
      if (err) throw err;

      console.log((reading.value*1000).toFixed());
    });
 }, 1000);
});
