document.addEventListener('DOMContentLoaded', function () {
    var copyUrlBtn = document.getElementById('copyUrlBtn');
    var quizUrlInput = document.getElementById('quizUrl');

    copyUrlBtn.addEventListener('click', function () {
        // Select the text inside the input field
        quizUrlInput.select();
        quizUrlInput.setSelectionRange(0, 99999); // For mobile devices

        // Copy the selected text to the clipboard
        document.execCommand('copy');

        // Deselect the text
        window.getSelection().removeAllRanges();

        // Change button text temporarily to indicate successful copy
        copyUrlBtn.textContent = 'Copied!';
        setTimeout(function () {
            copyUrlBtn.textContent = 'Copy URL';
        }, 2000); // Reset back to "Copy URL" after 2 seconds
    });
});
