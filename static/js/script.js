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
