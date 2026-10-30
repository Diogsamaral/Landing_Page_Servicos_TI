document.addEventListener('DOMContentLoaded', function () {
    const contactForm = document.getElementById('contactForm');
    const submitBtn = document.getElementById('submitBtn');
  
    if (!contactForm) return;
  
    contactForm.addEventListener('submit', async function (e) {
      e.preventDefault();
  
      // Feedback visual de carregamento no botão
      const originalBtnText = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fa-solid fa-spinner animate-spin"></i> Enviando...';
  
      const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        company: document.getElementById('company').value,
        phone: document.getElementById('phone').value,
        service_interest: document.getElementById('service_interest')?.value || '',
        message: document.getElementById('message').value
      };
  
      try {
        const response = await fetch('/api/leads/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(formData)
        });
  
        const result = await response.json();
  
        if (response.ok) {
          alert('🚀 Obrigado! Seu contato foi registrado com sucesso. Entraremos em contato em breve.');
          contactForm.reset();
        } else {
          alert('⚠️ Erro ao enviar: ' + (result.message || 'Tente novamente.'));
        }
      } catch (err) {
        console.error('Erro na requisição:', err);
        alert('⚠️ Erro de conexão ao enviar o formulário.');
      } finally {
        // Restaura o botão
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalBtnText;
      }
    });
  });
  