// Highlight active menu link
document.querySelectorAll('.sidebar a').forEach(link => {
    if (link.href === window.location.href) {
        link.style.background = '#044';
        link.style.fontWeight = 'bold';
    }
});

// Fade-in animation for content
document.addEventListener("DOMContentLoaded", () => {
    document.querySelector(".content").style.opacity = "1";
});
