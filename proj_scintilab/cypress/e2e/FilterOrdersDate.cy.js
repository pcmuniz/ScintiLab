// FAZER ESSE AQUI!!
describe('Filtro das ordens de serviço por data', () => {
    it('Eu, como funcionário, gostaria de filtrar as ordens de serviço por data', () => {
        cy.visit('http://127.0.0.1:8000/');
        cy.wait(60);
        cy.get('.custom-span > a').click();
        cy.wait(60);
        cy.get('#id_username').type('projetos2')
        cy.wait(60);
        cy.get('#id_password').type('cesar2024')
        cy.wait(60);
        cy.get('#customer-register-btn').click()
    })

})