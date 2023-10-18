$(document).ready(function() {
  // Khi bấm vào bất kỳ nút nào
  $(".custom-button").click(function() {
    // Lấy id của button
    var buttonId = $(this).attr("id");

    // Lấy giá trị từ ô input từ mục "search"
    var searchText = $("#searchText").val();

    // Gọi API endpoint 'search' để tìm kiếm
    $.ajax({
      url: '/search/',
      data: { searchText: searchText, buttonId: buttonId },
      method: 'GET',
      success: function(data) {

        var resultsContainer = $("#searchResults_1");
        resultsContainer.empty(); // Xóa nội dung hiện tại

        if (buttonId === "mainLinkButton" || buttonId === "relatedLinkButton" || buttonId === "allLinkButton") {
          // Nếu buttonID là "mainLinkButton", thì gắn hyperlink
          if (data.results.length > 2) {
              for (var i = 0; i < data.results.length; i += 2) {
                var title = data.results[i];
                var link = data.results[i + 1];

                // Tạo một phần tử a (hyperlink) và thiết lập các thuộc tính
                var linkElement = $("<a>");
                linkElement.attr("href", link);
                linkElement.text(title);

                // Thêm hyperlink vào container kết quả
                resultsContainer.append(linkElement);
                resultsContainer.append("<br>"); // Thêm dòng mới sau mỗi kết quả
              }
          } else {
                 resultsContainer.html( data.results);
             }
        } else if (buttonId === "vhmSearchButton") {

          if (data.results.length > 1) {
              for (var i = 0; i < data.results.length; i += 1) {
                // Thêm hyperlink vào container kết quả
                resultsContainer.append(data.results[i]);
                resultsContainer.append("<br>"); // Thêm dòng mới sau mỗi kết quả
              }
          } else {
                 resultsContainer.html( data.results);
          }

          // Thêm điều kiện cho buttonId là "relatedLinkButton"
          // Xử lý tương tự như trên, nếu cần
        } else if (buttonId === "kvSearchButton") {

              if (data.results.length > 2) {
                  for (var i = 0; i < data.results.length; i += 1) {
                    // Thêm hyperlink vào container kết quả
                    resultsContainer.append(data.results[i]);
                    resultsContainer.append("<br>"); // Thêm dòng mới sau mỗi kết quả
                  }
                 resultsContainer.append("<br>");
                 var linkElement = $("<a>");
                 linkElement.attr("href", data.results[5]);
                 linkElement.text(data.results[4]);
                 resultsContainer.append(linkElement);
                 resultsContainer.append("<br>");

              } else {
                     resultsContainer.html( data.results);
              }

          // Thêm điều kiện cho buttonId là "relatedLinkButton"
          // Xử lý tương tự như trên, nếu cần
        } else if (buttonId === "hnSearchButton") {

              if (data.results.length > 2) {
                  for (var i = 0; i < data.results.length; i += 1) {
                    // Thêm hyperlink vào container kết quả
                    resultsContainer.append(data.results[i]);
                    resultsContainer.append("<br>"); // Thêm dòng mới sau mỗi kết quả
                  }
                 resultsContainer.append("<br>");
                 var linkElement = $("<a>");
                 linkElement.attr("href", data.results[5]);
                 linkElement.text(data.results[4]);
                 resultsContainer.append(linkElement);
                 resultsContainer.append("<br>");

              } else {
                     resultsContainer.html( data.results);
              }

          // Thêm điều kiện cho buttonId là "relatedLinkButton"
          // Xử lý tương tự như trên, nếu cần
        }  else {
          // Nếu không phải "mainLinkButton", hiển thị data.results bình thường
          resultsContainer.html( data.results);
        }


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
    $("#searchResults_1").html("");
  });
});
