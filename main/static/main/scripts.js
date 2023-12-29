document.addEventListener('DOMContentLoaded', function() {
    var elementsToggleTop = document.querySelectorAll('[data-toggle="info"]');
    elementsToggleTop.forEach(function(element) {
        new bootstrap.Tooltip(element, {
        placement: 'top'
        });
    });

    var elementsToggleBottom = document.querySelectorAll('[data-toggle="dashboard"]');
    elementsToggleBottom.forEach(function(element) {
        new bootstrap.Tooltip(element, {
        placement: 'bottom'
        });
    });
});
