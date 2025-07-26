#!/bin/bash

# Масив з URL вебсайтів для перевірки
websites=(
  "https://google.com"
  "https://facebook.com"
  "https://twitter.com"
)

# Назва файлу логів
log_file="website_status.log"

# Очистити попередній файл логів
> "$log_file"

# Перевірка кожного сайту
for site in "${websites[@]}"; do
  # Отримання HTTP статус-коду з опрацюванням редиректів (-L)
  status_code=$(curl -s -o /dev/null -w "%{http_code}" -L "$site")

  if [ "$status_code" -eq 200 ]; then
    echo "$site is UP" | tee -a "$log_file"
  else
    echo "$site is DOWN" | tee -a "$log_file"
  fi
done

# Виведення повідомлення про завершення
echo "Результати перевірки записано у файл $log_file"
