// main.js

$(document).ready(function() {
  // Khi bấm vào bất kỳ nút nào
  $(".custom-button").click(function() {
    // Lấy id của button
    var buttonId = $(this).attr("id");

    // Lấy giá trị từ ô input từ mục "search"
    var searchText = $("#searchText").val();

    // Gọi API endpoint 'search' để tìm kiếm
    $.ajax({
      url: '/search/', // Điều này cần thay đổi nếu bạn đã cấu hình URL khác
      data: { searchText: searchText, buttonId: buttonId },
      method: 'GET',
      success: function(data) {
        // Hiển thị kết quả từ API lên ô "searchResults"
        $("#searchResults").val("Search Results: \n" + data.results);
      },
      error: function(error) {
        console.log(error);
      }
    });
  });

  // Khi bấm vào nút "Clear"
  $("#clearButton").click(function() {
    // Xóa nội dung của ô input "Search Text"
    $("#searchText").val("");
  });
});
