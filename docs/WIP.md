* Доделать logging всех алгоритмов
* Betcity -> Betsbs
* get_logger('prediction')
* Удалить граббер Betcity
* Ввести параметр (там, где надо) same_location
* Восстановить "via crosses"
* Восстановить "probabilities"
* log: caller
* Внедрить _get_fitted_runtime_strs
* **kwargs в комплексных предикторах
* При вызовах типа
  ```python
  (corners_home_count, corners_away_count) = count_events_of_teams_by_match_uuid(is_corner, match_header['uuid'])
  ```
  может возникать `TypeError`: функции типа `count_events_of_teams_by_match_uuid` возвращают `None`,
  когда не могут посчитать корректный ответ.
  Сейчас это искллючение ловится вручную, но ситуацию необходимо изменить в целом.
* Внедрить Chromeless/etc. (вместо Nightmare.JS)
