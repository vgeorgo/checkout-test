const formatNumber = (value, precision = 2) => parseFloat(value).toFixed(precision);

module.exports = {
  formatNumber,
}