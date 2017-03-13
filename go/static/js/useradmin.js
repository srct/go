/**
 * Filters a html table by hiding rows that do not contain the input string.
 * @param {html table} table - The table that we are searching through 
 * @param {String} input - The string we are searching through 
 */
function searchAndFilter(table, input) {
    // Cleanup the input search filter param
    let val = $.trim($(input).val()).replace(/ +/g, ' ').toLowerCase();

    // Filter the table rows based on the input string
    table.show().filter(function () {
        let text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
        return !~text.indexOf(val);
    }).hide();
}

// Grab the applied table
const $applied = $('#appliedTable tr:not(:first)');

$('#appliedInput').keyup(function () {
    searchAndFilter($applied, this);
});

// Grab the blocked table
const $blocked = $('#blockedTable tr:not(:first)');

$('#blockedInput').keyup(function () {
    searchAndFilter($blocked, this);
});

// Grab the current table
const $current = $('#currentTable tr:not(:first)');

$('#currentInput').keyup(function () {
    searchAndFilter($current, this);
});

