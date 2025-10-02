from abc import ABC, abstractmethod
# -------------------------
class Produto(ABC):
    def __init__(self, nome: str, preco_base: float):
        self.nome = nome
        self.preco_base = preco_base

    @abstractmethod
    def calcular_preco_final(self) -> float:
        """Contrato: toda subclasse deve implementar o cálculo do preço final"""
        pass

    @abstractmethod
    def detalhar(self) -> str:
        """Contrato: retorna uma string com os detalhes do produto"""
        pass
# -------------------------
class ProdutoFisico(Produto):
    def __init__(self, nome: str, preco_base: float, custo_frete: float):
        super().__init__(nome, preco_base)
        self.custo_frete = custo_frete

    def calcular_preco_final(self) -> float:
        return self.preco_base + self.custo_frete

    def detalhar(self) -> str:
        return (f"{self.nome:<25} | Base: R$ {self.preco_base:6.2f} | "
                f"Frete: R$ {self.custo_frete:6.2f} | "
                f"Total: R$ {self.calcular_preco_final():6.2f}")
# -------------------------
class ProdutoDigital(Produto):
    def __init__(self, nome: str, preco_base: float, taxa_servico: float):
        super().__init__(nome, preco_base)
        self.taxa_servico = taxa_servico

    def calcular_preco_final(self) -> float:
        return self.preco_base + self.taxa_servico

    def detalhar(self) -> str:
        return (f"{self.nome:<25} | Base: R$ {self.preco_base:6.2f} | "
                f"Taxa: R$ {self.taxa_servico:6.2f} | "
                f"Total: R$ {self.calcular_preco_final():6.2f}")
# -------------------------
def mostrar_carrinho(carrinho: list[Produto]) -> None:
    total_produtos = 0
    total_geral = 0

    print("=" * 70)
    print(" " * 25 + "CUPOM FISCAL - LOJA VIRTUAL")
    print("=" * 70)
    print(f"{'Produto':<25} | {'Base':<13} | {'Frete/Taxa':<13} | {'Total':<10}")
    print("-" * 70)

    for produto in carrinho:
        print(produto.detalhar())
        total_produtos += produto.preco_base
        total_geral += produto.calcular_preco_final()

    print("-" * 70)
    print(f"{'Total Produtos (sem frete/taxa)':<40} R$ {total_produtos:6.2f}")
    print(f"{'Total Geral (com frete/taxa)':<40} R$ {total_geral:6.2f}")
    print("=" * 70)
# -------------------------
if __name__ == "__main__":
    carrinho = [
        ProdutoFisico("Livro de Python", 50.0, 10.0),
        ProdutoFisico("Caneca Dev", 30.0, 5.0),
        ProdutoDigital("E-book Django", 40.0, 2.0),
        ProdutoDigital("Curso Online POO", 120.0, 15.0),
    ]

    mostrar_carrinho(carrinho)