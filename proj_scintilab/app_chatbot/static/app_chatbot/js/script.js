const chatContainer = document.getElementById('chat-window');
const userInput = document.getElementById('user-input');

// Variável para armazenar o contexto da conversa
let conversationContext = '';

// Função para adicionar mensagens do chat ao contêiner
function addMessageToChat(message) {
    const messageElement = document.createElement('div');
    messageElement.innerHTML = message;
    chatContainer.appendChild(messageElement);
}

function clearChat() {
    chatContainer.innerHTML = '';
}


function processUserInput(input) {
    switch(conversationContext) {
        case '':
            if (input.toLowerCase() === '1') {
                clearChat();
                addMessageToChat('Nesse caso, me parece que você precisa criar uma ordem de serviço para que a nossa assistência técnica possa resolver o seu problema.');
                addMessageToChat('A ordem de serviço é um formulário no qual você deve preencher suas informações para que possamos dar continuidade ao atendimento.');
                addMessageToChat('Deseja ir adiante?<br><br>1 - Sim, gostaria!<br>2 - Não, obrigado!');
                addMessageToChat('Por favor, digite abaixo o número correspondente à opcão desejada.');
                conversationContext = '';
                userInput.value = '';
                showChatModal();
                
            } else {
                addMessageToChat('Quando a mensagem foge dos ifs');
            }
            break;

        default:
            addMessageToChat('Desculpe, houve um erro na conversa.');
    }
}

userInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        const userMessage = userInput.value;
        addMessageToChat(`Você: ${userMessage}`);
        processUserInput(userMessage);
        userInput.value = '';
    }
});

function toggleChatModal() {
    const modal = document.getElementById('chat-modal');
    modal.style.display = modal.style.display === 'block' ? 'none' : 'block';
}

document.getElementById('chat-icon').addEventListener('click', toggleChatModal);

document.querySelector('.close').addEventListener('click', toggleChatModal);

addMessageToChat('Olá, Tudo bem?<br> Eu sou a assistente virtual da Eceel-tec e estou encarregada do seu atendimento.<br> Do que você precisa?');
addMessageToChat('<br>1 - Meu eletrodoméstico está com problema<br>2 - Acompanhar ordem de serviço<br>3 - Gerar orçamento');
addMessageToChat('<br>Por favor, digite abaixo o número correpondente à opcão desejada.');