let protocolo;

before(() => {
    cy.visit('http://127.0.0.1:8000/');
    cy.wait(60);
    cy.get('.btn').click();
    cy.wait(60);
    cy.get('#bb-0').click();
    cy.wait(60);

    // Dados do cliente
    cy.get('#id_client_name').type('Gabriel Ramos')
    cy.wait(60);
    cy.get('#id_client_cpf_cnpj').type('00000000000');
    cy.wait(60);
    cy.get('#id_client_rg_ie').type('0000000')
    cy.wait(60);
    cy.get('#id_client_birthdate').type('01/01/1990')
    cy.wait(60);
    cy.get('#id_client_email').type('gramos@cesar.school')
    cy.wait(60);
    cy.get('#id_client_cellphone').type('5581000000000')
    cy.wait(60);
    cy.get('#id_client_telephone').type('0000000000000')
    cy.wait(60);
    cy.get('#id_client_adress').type('Rua do Brum, 77')
    cy.wait(60);
    cy.get('#id_client_neighborhood').type('Recife Antigo')
    cy.wait(60);
    cy.get('#id_client_zip').type('50030260')
    cy.wait(60);
    cy.get('#id_client_city').type('Recife')
    cy.wait(60);
    cy.get(':nth-child(8) > :nth-child(4) > .form-control').select('PE')
    cy.wait(60);
    cy.get('#dados-comprador-tab').click()
    cy.wait(60);

    // Dados do comprador
    cy.get('#id_buyer_name').type('Gabriel Ramos')
    cy.wait(60);
    cy.get('#id_buyer_cpf_cnpj').type('00000000000');
    cy.wait(60);
    cy.get('#id_buyer_rg_ie').type('0000000')
    cy.wait(60);
    cy.get('#id_buyer_birthdate').type('01/01/1990')
    cy.wait(60);
    cy.get('#id_buyer_email').type('gramos@cesar.school')
    cy.wait(60);
    cy.get('#id_buyer_cellphone').type('5581000000000')
    cy.wait(60);
    cy.get('#id_buyer_telephone').type('0000000000000')
    cy.wait(60);
    cy.get('#id_buyer_adress').type('Rua do Brum, 77')
    cy.wait(60);
    cy.get('#id_buyer_neighborhood').type('Recife Antigo')
    cy.wait(60);
    cy.get('#id_buyer_zip').type('50030260')
    cy.wait(60);
    cy.get('#id_buyer_city').type('Recife')
    cy.wait(60);
    cy.get(':nth-child(5) > .form-control').select('PE')
    cy.wait(60);
    cy.get('#dados-aparelho-tab').click()
    cy.wait(60);

    // Dados do aparelho
    cy.get('#id_store_name').type('Amazon')
    cy.wait(60);
    cy.get('#id_receipt_number').type('3341541961217052194169612719616092908092950')
    cy.wait(60);
    cy.get('#id_purchase_date').type('01/01/2022')
    cy.wait(60);
    cy.get('#id_product_code').type('BRA_202219')
    cy.wait(60);
    cy.get('#id_price').type('2593.9')
    cy.wait(60);
    cy.get('#id_equipment_name').type('Geladeira')
    cy.wait(60);
    cy.get('#id_model').type('Três portas')
    cy.wait(60);
    cy.get('#id_brand').type('Eletrolux')
    cy.wait(60);
    cy.get('#id_serial_number').type('591283')
    cy.wait(60);
    cy.get('#id_user_password').type('abc')
    cy.wait(60);
    cy.get('#id_defect').type('Nenhum')
    cy.wait(60);
    cy.get('#dados-aparelho > :nth-child(7) > :nth-child(1) > .form-control').select('Rompido')
    cy.wait(60);
    cy.get('#dados-aparelho > :nth-child(7) > :nth-child(2) > .form-control').select('Novo - sem funcionar')
    cy.wait(60);
    cy.get('#id_acessories').type('Nenhum')
    cy.wait(60);
    cy.get('#id_files').type('Nenhum')
    cy.wait(60);
    cy.get('#id_observations').type('A porta não abre direito')
    cy.wait(60);
    cy.get('.btn').click()
    cy.wait(60);
    cy.get('.alert')
    
});


describe('cliente vai ver o status da ordem de serviço dele', () => {
    it('cenario1', () => {
        
        // cy.visit('http://127.0.0.1:8000/');
        // cy.wait(60);
        // cy.get('.btn').click();
        // cy.wait(60);
        // cy.get('#bb-1').click()
        // cy.wait(60);
        // cy.get('[type="text"]').type(protocolo)
        // cy.wait(60);
        // cy.get('.search-button').click()
        // cy.wait(60);
        // Adicione qualquer outra ação necessária aqui
    });
});
