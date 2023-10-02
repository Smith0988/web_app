// main.js

$(document).ready(function() {
  // Khi bấm vào bất kỳ nút nào
  $(".custom-button").click(function() {
    // Lấy id của button
    var buttonId = $(this).attr("id");

    // Lấy giá trị từ ô input từ mục "search"
    var searchText = $("#searchText").val();

    // Hiển thị id của button và giá trị của ô input trong ô kết quả
    var currentResults = $("#searchResults").val(); // Lấy giá trị hiện tại của ô kết quả
    var newResults = "Button ID: " + buttonId + "\nSearch Text: " + searchText;

    // Nối giá trị mới vào giá trị hiện tại của ô kết quả
    $("#searchResults").val(currentResults + "\n" + newResults);
  });
});
