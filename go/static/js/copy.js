/*
 * Script for copying text and displaying a tooltip.
 */

var clipboard = new Clipboard('#copy-button');

$('#copy-button').tooltip({
    trigger: 'hover',
    placement: 'bottom'
});

$('#copy-button').on('hidden.bs.tooltip', function () {
    $('#copy-button').attr('data-original-title', 'Copy to Clipboard');
});

clipboard.on('success', function (e) {
    e.clearSelection();
    $('#copy-button').attr('data-original-title', 'Copied!').tooltip('show');
});


