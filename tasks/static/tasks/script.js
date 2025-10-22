// Smooth fade-in effect for newly loaded tasks
document.addEventListener('DOMContentLoaded', () => {
    const tasks = document.querySelectorAll('.task');
    tasks.forEach((task, index) => {
        task.style.opacity = 0;
        setTimeout(() => { task.style.opacity = 1; task.style.transition = 'opacity 0.5s'; }, index * 100);
    });
});
