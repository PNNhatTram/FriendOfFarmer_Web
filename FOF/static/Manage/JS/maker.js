
		const confirmButtons = document.querySelectorAll('.confirm-btn');

		confirmButtons.forEach((button) => {
			button.addEventListener('click', function() {
				alert('Bạn đã xác nhận thành công');
			});
		});
