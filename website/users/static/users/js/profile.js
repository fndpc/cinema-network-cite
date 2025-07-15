document.addEventListener("DOMContentLoaded", () => {
  const qrButtons = document.querySelectorAll(".qr-button")
  const qrModal = document.getElementById("qr-modal")
  const qrModalClose = document.querySelector(".qr-modal-close")
  const qrCodeImage = document.getElementById("qr-code-image")

  // Открытие модального окна с QR-кодом
  qrButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const qrUrl = this.getAttribute("data-qr-url")
      if (qrUrl) {
        qrCodeImage.src = qrUrl
        qrModal.style.display = "block"
        document.body.style.overflow = "hidden"
      }
    })
  })

  // Закрытие модального окна
  if (qrModalClose) {
    qrModalClose.addEventListener("click", () => {
      qrModal.style.display = "none"
      document.body.style.overflow = ""
    })
  }

  // Закрытие модального окна при клике вне его содержимого
  if (qrModal) {
    qrModal.addEventListener("click", (event) => {
      if (event.target === qrModal) {
        qrModal.style.display = "none"
        document.body.style.overflow = ""
      }
    })
  }

  // Закрытие модального окна по нажатию Escape
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && qrModal && qrModal.style.display === "block") {
      qrModal.style.display = "none"
      document.body.style.overflow = ""
    }
  })
})
