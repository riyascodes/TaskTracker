document.querySelectorAll('.actions a[href*="delete_task"]').forEach(link => {
    link.addEventListener('click', function(e) {
        if (!confirm('Are you sure you want to delete this task?')) {
            e.preventDefault();
        }
    });
});
