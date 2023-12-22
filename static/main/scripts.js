document.addEventListener('DOMContentLoaded', function() {
    var elements = document.querySelectorAll('[data-toggle="info"]');
    elements.forEach(function(element) {
        new bootstrap.Tooltip(element, {
        placement: 'bottom'
        });
    });
});
