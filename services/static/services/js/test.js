

let tarifNumber;

    

document.getElementById("button1").addEventListener('click', openModal)
document.getElementById('button2').addEventListener('click', openModal)
document.getElementById('button3').addEventListener('click', openModal)
document.getElementById('button4').addEventListener('click', openModal)
document.getElementById('requestForm').addEventListener('submit', confirmApplication)



  function openModal(event) {
    document.getElementById("modal").style.display = 'block';
    event.preventDefault();
    tarifNumber = event.target.getAttribute('tarifnumber')
  }

  document.getElementById("modal-close").onclick = function() {
      document.getElementById("modal").style.display = 'none';
  };

  // Закрытие модального окна при клике вне его
//   window.onclick = function(event) {
//       if (event.target == document.getElementById("modal")) {
//           document.getElementById("modal").style.display = 'none';
//       }
//   };

  function confirmApplication(event){
      event.preventDefault();
      alert(`Имя: ${document.getElementById('firstName').value}, Фамилия: ${document.getElementById('lastName').value}, 
      Номер телефона: ${document.getElementById('mobile').value}, Адрес: ${document.getElementById('address').value}`);
      console.log("Текущий тариф: " + tarifNumber);
      document.getElementById("modal").style.display = 'none';
      this.reset();
  }


