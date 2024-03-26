async function getData(url) {
    try {
        const response = await fetch(url);
        return await response.json();
    } catch (error) {
        return console.error('Erro na requisição GET:', error);
    }
}

document.addEventListener("DOMContentLoaded", function() {  
    document.getElementById('linkProdutos').addEventListener('click', function(event) {
        event.preventDefault();
        let produtosHTML = '<h2>Produtos</h2>';
        document.getElementById('conteudo').innerHTML = produtosHTML;
        getData('http://127.0.0.1:8002/produtos')
            .then(data => {
                let productsList = "<ul>"
                data.forEach(produto => {
                   productsList += `<li>${produto.nome} - ${produto.preco}</li>`;
                });
               productsList += '</ul>';
                // Exibir os produtos na div "conteudo"
                document.getElementById('conteudo').innerHTML+=productsList;
            })
            .catch(error => console.error('Erro ao obter os produtos:', error));
    });

    document.getElementById('linkLogin').addEventListener('click', function(event) {
        event.preventDefault();
        // Exibir o formulário de login
        document.getElementById('conteudo').innerHTML = `
            <h2>Formulário de Login</h2>
            <form id="loginForm">
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username"><br>
                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password"><br><br>
                <button type="submit">Login</button>
            </form>
        `;
        // Adicionar evento de envio do formulário
        document.getElementById('loginForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const username = formData.get('username');
            const password = formData.get('password');
            
            fetch('http://127.0.0.1:8001/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'sucesso') {
                    alert(data.mensagem);
                } else {
                    alert(data.mensagem);
                }
            })
            .catch(error => console.error('Erro ao fazer login:', error));
        });
    });

    document.getElementById('linkPedido').addEventListener('click', function(event) {
        event.preventDefault();
        // Exibir a lista de pedidos do usuário
        let pedidosHTML = 
        `
            <h2>Pedidos</h2>
            <input placeholder="Digite o id do usuário" id="user-id">
            <button onclick="consultarPedidos()">Consultar</button>

            <ul id="pedidos-list"></ul>
        `;
        document.getElementById('conteudo').innerHTML = pedidosHTML;
    });

    document.getElementById('linkCarrinho').addEventListener('click', function(event) {
        event.preventDefault();
        // Exibir o carrinho do usuário
        fetch('http://127.0.0.1:8003/carrinho/1') // Supondo que o ID do usuário seja 1
            .then(response => response.json())
            .then(data => {
                // Montar o HTML com os itens do carrinho
                let carrinhoHTML = '<h2>Carrinho</h2><ul>';
                data.itens.forEach(item => {
                    carrinhoHTML += `<li>${item.produto_id} - ${item.quantidade}</li>`;
                });
                carrinhoHTML += '</ul>';
                
                document.getElementById('conteudo').innerHTML = carrinhoHTML;
            })
            .catch(error => console.error('Erro ao obter o carrinho:', error));
    });
});

// Funções do sistema
function consultarPedidos(){
    getData('http://127.0.0.1:8004/pedidos/' + document.getElementById("user-id").value) // Supondo que o ID do usuário seja 432
        .then(data => {
            console.log(data)
            let pedidosList = document.getElementById("pedidos-list");
            pedidosList.innerHTML = ""

            // Montar o HTML com a lista de pedidos
            data.forEach(pedido => {
                pedidosList.innerHTML += `<li>Order ID: ${pedido.order_id}, User ID: ${pedido.user_id}</li>`;
            });
            pedidosList.innerHTML += '</ul>';
    
        })
        .catch(error => console.error('Erro ao obter os pedidos:', error));
}