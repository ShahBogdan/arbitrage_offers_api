from django.db import models


class Faq(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.CharField(max_length=255, verbose_name="Запитання")
    answer = models.TextField(verbose_name="Відповідь")
    show_in_main = models.BooleanField(
        default=False, verbose_name="На головну")

    def __str__(self):
        return self.question
