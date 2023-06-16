# Generated by Django 4.2.1 on 2023-06-16 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="이메일 주소"
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="비밀 번호")),
                (
                    "join_date",
                    models.DateTimeField(auto_now_add=True, verbose_name="가입일"),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CheckEmail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="인증용 이메일"
                    ),
                ),
                (
                    "code",
                    models.CharField(max_length=6, unique=True, verbose_name="확인용 코드"),
                ),
                ("try_num", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="그룹 이름")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성일"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="업데이트"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("0", "활성화"),
                            ("1", "비활성화"),
                            ("2", "강제중지"),
                            ("3", "삭제"),
                        ],
                        default="0",
                        max_length=1,
                        verbose_name="상태",
                    ),
                ),
                (
                    "master",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="master_group",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="그룹장",
                    ),
                ),
                (
                    "members",
                    models.ManyToManyField(
                        blank=True,
                        related_name="user_group",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="멤버",
                    ),
                ),
            ],
        ),
    ]
