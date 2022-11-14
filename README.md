
# FilmLogger API

As exposure meters usually don't work anymore with old film cameras, you have to use an application that gets the EV from your phone's camera and suggests a suitable combination of shutter speed and aperture. 

This small API was developed for a web application that would extract EV from EXIF tags of an uploaded photo and suggest settings for your film camera. However, I discovered that iPhones delete EXIF data from photos uploaded through a browser, so I never finished the front-end part.

## API

The API is built using FastAPI, and its responses are based on the [Google JSON Style Guide](https://google.github.io/styleguide/jsoncstyleguide.xml "Google JSON Style Guide").

#### /ISO
* `GET` : Get a list of possible ISO values

#### /Shutter
* `GET` : Get a list of possible shutter speed values with nominal (for display) and precise (for calculations) values

#### /Aperture
* `GET` : Get a list of possible aperture values with nominal (for display) and precise (for calculations) values

#### /EV
* `GET` : Get all possible combinations of shutter speed and aperture per EV (the so-called EV chart)

#### /Photo
* `POST` : It receives an image, extracts EXIF tags, and calculates EV for a given film ISO. The result is all combinations of shutter speed and aperture from the EV chart

## Credits

This [article](https://www.scantips.com/lights/evchart.html "article") was of great help in understanding EV.
