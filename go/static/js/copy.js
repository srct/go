/*
 * Script for copying text and displaying a tooltip.
 */

$('#btn').tooltip({
    trigger: 'click',
    placement: 'bottom'
});

function setTooltip(button, message) {
    $(button).tooltip('hide').attr('data-original-title', message)
        .tooltip('show');
}

function hideTooltip(button) {
    window.setTimeout(function() {
        $(button).tooltip('hide');
    }, 700);
}

var clipboard = new Clipboard('#btn');

clipboard.on('success', function(e) {
    e.clearSelection();
    setTooltip(e.trigger, 'Copied!');
    hideTooltip(e.trigger);
});
