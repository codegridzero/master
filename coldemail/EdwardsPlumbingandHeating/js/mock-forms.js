document.addEventListener('DOMContentLoaded', function () {
    const forms = document.querySelectorAll('.w-form form');
    forms.forEach(function (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            e.stopPropagation();
            const parent = form.closest('.w-form');
            if (parent) {
                form.style.display = 'none';
                const done = parent.querySelector('.w-form-done');
                if (done) done.style.display = 'block';
                const fail = parent.querySelector('.w-form-fail');
                if (fail) fail.style.display = 'none';
            }
        });
    });
});
