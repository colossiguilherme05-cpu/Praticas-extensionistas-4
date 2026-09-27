from django.db import models
from django.core.validators import RegexValidator


class Paciente(models.Model):
    nome_pac = models.CharField(max_length=100)
    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{11}$',
                message='O CPF deve conter exatamente 11 números.'
            )
        ]
    )
    datanasc = models.DateField()
    numtelefone = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'^\d{10,11}$',
                message='O telefone deve conter 10 ou 11 números.'
            )
        ]
    )
    email = models.EmailField()
    senha = models.CharField(max_length=24)

    def __str__(self):
        return self.nome_pac


class Especialidade(models.Model):
    nome_esp = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_esp


class ProfissionalSaude(models.Model):
    nome_prof = models.CharField(max_length=100)
    crm_prof = models.CharField(max_length=20, unique=True)
    id_esp = models.ForeignKey(Especialidade, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_prof


class UnidadeSaude(models.Model):
    nome_uni = models.CharField(max_length=100)
    endereco_uni = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_uni


class Consulta(models.Model):
    STATUS = [
        ("AGENDADA", "Agendada"),
        ("CANCELADA", "Cancelada"),
        ("REALIZADA", "Realizada"),
    ]

    data_con = models.DateField()
    hora_con = models.TimeField()
    status_con = models.CharField(max_length=50, choices=STATUS, default="AGENDADA")

    id_pac = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    id_prof = models.ForeignKey(ProfissionalSaude, on_delete=models.PROTECT)
    id_uni = models.ForeignKey(UnidadeSaude, on_delete=models.PROTECT)
    observacoes = models.CharField(max_length=255, null=True, blank=True)


class Medicamento(models.Model):
    nome_med = models.CharField(max_length=100)
    desc_med = models.CharField(max_length=255, null=True, blank=True)
    estoque = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nome_med


class SolicitacaoMedicamento(models.Model):
    STATUS = [
        ("PENDENTE", "Pendente"),
        ("APROVADA", "Aprovada"),
        ("CANCELADA", "Cancelada"),
    ]

    data_solic = models.DateField(auto_now_add=True)
    status_solic = models.CharField(max_length=50, choices=STATUS, default="PENDENTE")

    id_pac = models.ForeignKey(Paciente, on_delete=models.PROTECT)

    def __str__(self):
        return f"Solicitação {self.id}"


class ItemSolicitacao(models.Model):
    id_solic = models.ForeignKey(SolicitacaoMedicamento, on_delete=models.CASCADE)
    id_med = models.ForeignKey(Medicamento, on_delete=models.PROTECT)
    quant_itemsolic = models.DecimalField(max_digits=20, decimal_places=1)

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return self.nome
    
