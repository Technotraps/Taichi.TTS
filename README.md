# Taichi.TTS (без вокодера)


**DISCLAIMER :- Следующая кодовая база была изменена в соответствии с документом [Learning to Speak Fluently in a Foreign Language:Multilingual Speech Synthesis and Cross-Language Voice Cloning](https://arxiv.org/pdf/1907.04448.pdf)**

## Формат набора данных
Модели необходимо предоставить 2 текстовых файла, один для обучения и один для валидации. Каждая строка txt-файла должна иметь следующий формат :-. 
```
<path-to-wav-file>|<text-corresponding-to-speech-in-wav>|<speaker-no>|<lang-no>
```

```<speaker-no> варьируется от 0 до n-1, где n - количество дикторов.```

```<lang-no> от 0 до m-1, где m - количество языков.```

## Hparams
```hparams.training_files, hparams.validation_files``` должны быть установлены на пути к txt файлам из предыдущего раздела.

```hparams.n_speakers, hparams.dim_yo``` нужно изменить на количество дикторов.

```hparams.n_langs``` должны быть установлены на количество языков.

Чтобы изменить языки, добавьте/удалите символы юникода в переменной ```_letters`` в ``text/symbols.py``` .

## TODO 
- [ ] Модифицировать код в соответствии с бумагами: [Wave-Tacotron: Spectrogram-free end-to-end text-to-speech synthesis](https://arxiv.org/pdf/2011.03568.pdf), [Non-Attentive Tacotron: Robust and Controllable Neural TTS Synthesis Including Unsupervised Duration Modeling](https://arxiv.org/pdf/2010.04301.pdf)
- [ ] Тренировать русскоанглийскую модель (в процессе)
- [ ] Сделать дружелюбный интерфейс
