document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('form').addEventListener('submit', function (e) {
        e.preventDefault(); // Ngăn chặn gửi form mặc định

        const query = document.getElementById('query').value;

        // Gửi truy vấn AJAX đến view Django
        fetch('/search/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: `query=${encodeURIComponent(query)}`
        })
        .then(response => response.json())
        .then(data => {
            // Hiển thị kết quả tìm kiếm
            const resultsList = document.querySelector('ul');
            resultsList.innerHTML = '';
            data.results.forEach(result => {
                const listItem = document.createElement('li');
                listItem.textContent = result;
                resultsList.appendChild(listItem);
            });
        });
    });

    // Hàm lấy giá trị của cookie CSRF
    function getCookie(name) {
        const cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Kiểm tra xem cookie có tên là csrfmiddlewaretoken không
                if (cookie.substring(0, name.length + 1) === name + '=') {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
