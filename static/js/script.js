function updateCodename() {
    const courseSelect = document.getElementById('id_course');
    const selectedCourseText = courseSelect.options[courseSelect.selectedIndex].text
    const day = document.getElementById('id_usual_day').value;
    const time = document.getElementById('id_usual_time').value;

    if (selectedCourseText && day && time) {
        const codename = `${selectedCourseText}_${day}_${time}`;
        document.getElementById('id_codename').value = codename;
    }
}

function validateForm() {
    const codename = document.getElementById('id_codename').value;
    if (!codename) {
        alert('Codename cannot be empty!');
        return false;
    }
    return true;
}

document.addEventListener('DOMContentLoaded', function() {
        // Get all forms on the page
        const forms = document.querySelectorAll('form[id^="update-form-"]');
        
        // Loop through all forms and attach the onsubmit event
        forms.forEach(function(form) {
            form.onsubmit = function(event) {
                event.preventDefault();  // Prevent form submission

                // Get the lesson's ID (from the form's ID)
                const lessonId = form.id.split('-').pop();
                
                // Show the confirmation dialog
                const userConfirmed = confirm("Do you want to save the changes for this lesson?");

                // If user clicked 'Yes', set the hidden field and submit the form
                if (userConfirmed) {
                    document.getElementById("confirmation_response_" + lessonId).value = "yes";
                    form.submit();  // Now submit the form
                } else {
                    // If user clicked 'No', set the hidden field and do not submit
                    document.getElementById("confirmation_response_" + lessonId).value = "no";
                }
            };
        });
    });