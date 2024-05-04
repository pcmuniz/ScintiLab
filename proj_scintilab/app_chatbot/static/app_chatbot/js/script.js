import Alpine from "https://cdn.skypack.dev/alpinejs@3.11.1";

const mockTypingAfter = 1500;
const mockResponseAfter = 3000;
const mockOpeningMessage =
  "Olá, sou a atendente virtual da Eceel-Tec e vou realizar o seu atendimento!\nPosso te ajudar das seguintes formas:\n1 - Consertar o meu eletrodoméstico\n2 - Acompanhar o andamento do conserto\n3 - Agendar a visita de um técnico\nDigite o número correspondente à opção desejada:";
const mockResponsePrefix = "Você escolheu: ";

document.addEventListener("alpine:init", () => {
  Alpine.data("chat", () => ({
    newMessage: "",
    showTyping: false,
    waitingOnResponse: true,
    messages: [],
    init() {
      this.mockResponse(mockOpeningMessage);
    },
    sendMessage() {
      if (this.waitingOnResponse) return;
      this.waitingOnResponse = true;
      this.messages.push({ role: "user", body: this.newMessage });
      this.newMessage = "";
      window.scrollTo(0, 0);
      this.mockResponse();
    },
    typeOutResponse(message) {
      this.messages.push({ role: "assistant", body: "", beingTyped: true });
      let responseMessage = this.messages[this.messages.length - 1];
      let i = 0;
      let interval = setInterval(() => {
        responseMessage.body += message.charAt(i);
        i++;
        if (i > message.length - 1) {
          this.waitingOnResponse = false;
          delete responseMessage.beingTyped;
          clearInterval(interval);
        }
      }, 30);
    },
    mockResponse(message) {
      setTimeout(() => {
        this.showTyping = true;
      }, mockTypingAfter);
      setTimeout(() => {
        this.showTyping = false;
        // TODO: if else
        let responseMessage =
          message ??
          mockResponsePrefix + this.messages[this.messages.length - 1].body;
        this.typeOutResponse(responseMessage);
      }, mockResponseAfter);
    }
  }));
});

Alpine.start();