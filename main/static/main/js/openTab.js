function openTab(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent"); // получает список всех элементов с данным классом
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none"; // через цикл меняем свойство у каждого элемента
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks"); // получает список всех элементов с данным классом
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", ""); // через цикл удаляем класс у каждого элемента
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block"; // получаем элемент с id и меняем его свойство
    evt.currentTarget.className += " active"; // получаем элемент на котором обрабатывает событие и добавляем к имени его класса еще один
}

document.getElementById("defaultOpen").click();