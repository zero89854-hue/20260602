{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM0kKiWbW84QqQvBsrDX8G3",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/zero89854-hue/20260602/blob/main/20260607_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8tKd8g8sq_qf",
        "outputId": "10ce6e72-acde-4bcc-c5a2-30b5b25a4740"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "輸入今天日期20260607\n",
            "正確\n"
          ]
        }
      ],
      "source": [
        "date=int(input(\"輸入今天日期\"))\n",
        "answer=20260607\n",
        "if date==answer:\n",
        "  print(\"正確\")\n",
        "else:\n",
        "  print(\"錯誤\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#for迴圈與range\n",
        "for x in range(1,11):\n",
        "  print (x, end=\" \")\n",
        "\n",
        "for x in range(0,20,2):\n",
        "  print(x, end=\" \")\n",
        "\n",
        "#"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RbEPh1q4uD1Y",
        "outputId": "51a03430-400f-4ca5-d942-df0404f022c8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 4 5 6 7 8 9 10 0 2 4 6 8 10 12 14 16 18 "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"20260608\")\n",
        "\n",
        "#"
      ],
      "metadata": {
        "id": "jiXIRQGnuSyJ"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#計算1～100之間，3的倍數的總和\n",
        "sum=0\n",
        "count=0\n",
        "for x in range(1,101):\n",
        "    sum+=count\n",
        "    count+=3\n",
        "print(\"total=\",sum)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DdCOkAMloPkz",
        "outputId": "08c323da-ded3-45c3-a812-6b04da0859b5"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "total= 14850\n"
          ]
        }
      ]
    }
  ]
}