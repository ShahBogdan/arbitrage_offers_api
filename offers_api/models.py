from django.db import models


class Advantages(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return self.text


class RepaymentMethods(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return self.text


class Documents(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return self.text


class Offer(models.Model):
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, verbose_name='Назва')
    offer_url = models.URLField(verbose_name='Посилання на оффер')
    image = models.ImageField(upload_to='offers/', verbose_name='Лого офферу')
    first_amount = models.IntegerField(
        verbose_name='Перший кредит - макс грн.')
    second_amount = models.IntegerField(
        verbose_name='Повторний кредит макс грн.')
    amount_from = models.IntegerField(verbose_name='Кредит від грн.')
    percent_per_day = models.DecimalField(
        max_digits=15, decimal_places=4, verbose_name='Відсотків на день')
    term_from = models.IntegerField(verbose_name='Кредит від - днів')
    term_to = models.IntegerField(verbose_name='Кредит до - днів')
    real_annual_rate_from = models.DecimalField(
        max_digits=15, decimal_places=4, verbose_name='Реальна річна ставка від')
    real_annual_rate_to = models.DecimalField(
        max_digits=15, decimal_places=4, verbose_name='Реальна річна ставка до')
    days_rate = models.DecimalField(
        max_digits=15, decimal_places=4, verbose_name='Денна відсодкова ставка')
    advantages = models.ManyToManyField(
        Advantages,  blank=True, verbose_name='Переваги')
    repayment_methods = models.ManyToManyField(
        RepaymentMethods,  blank=True,  verbose_name='Способи погашення')
    documents = models.ManyToManyField(
        Documents,  blank=True, verbose_name='Документи')
    age = models.IntegerField(verbose_name='Вік до')

    time_to_get = models.IntegerField(verbose_name='Час на отримання коштів')
    on_lending = models.BooleanField(verbose_name='Перекредитування')
    cash = models.BooleanField(verbose_name='Готівкою')
    bank_card = models.BooleanField(verbose_name='На банківську картку')
    bankID = models.BooleanField(verbose_name='Верифікація через bankID')
    around_the_clock = models.BooleanField(verbose_name='Цілодобово')
    basic_characteristics_href = models.URLField(
        verbose_name='Посилання на Істотні характеристики послуги')
    user_warning = models.URLField(
        verbose_name='Посилання на попередження для користувача')
    license = models.CharField(max_length=200, verbose_name='Ліцензія')
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(max_length=200, verbose_name='Адреса')
    phone = models.CharField(max_length=200, verbose_name='Телефон')
    zero_first = models.BooleanField(
        default=False, verbose_name='Перший під 0% ?')
    legal_entity = models.CharField(
        max_length=200, verbose_name='Юридична особа')
    recommended = models.BooleanField(
        default=False, verbose_name='Рекомендовано')
    show_offer = models.BooleanField(
        default=True, verbose_name='Активний оффер ?')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
