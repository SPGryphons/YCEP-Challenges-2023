const eyeball = document.querySelector(".ball");
const button = document.getElementById("button");

document.onmousemove = () => {
    const x = event.clientX * 100 / window.innerWidth + "%";
    const y = event.clientY * 100 / window.innerHeight + "%";

    eyeball.style.left = x;
    eyeball.style.top = y;
}

button.addEventListener('focus', function () {
    button.disabled = true;
});

button.addEventListener('blur', function () {
    button.disabled = false;
});

button.addEventListener('mouseenter', function () {
    button.disabled = true;
});

button.addEventListener('mouseleave', function () {
    button.disabled = false;
});


// ============================= TESTING CODE =============================

// /**
//  * --------------------------------------------------------------------------
//  * Bootstrap button.js
//  * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
//  * --------------------------------------------------------------------------
//  */

// import BaseComponent from './base-component.js'
// import EventHandler from './dom/event-handler.js'
// import { defineJQueryPlugin } from './util/index.js'

// /**
//  * Constants
//  */

// const NAME = 'button'
// const DATA_KEY = 'bs.button'
// const EVENT_KEY = `.${DATA_KEY}`
// const DATA_API_KEY = '.data-api'

// const CLASS_NAME_ACTIVE = 'active'
// const SELECTOR_DATA_TOGGLE = '[data-bs-toggle="button"]'
// const EVENT_CLICK_DATA_API = `click${EVENT_KEY}${DATA_API_KEY}`

// /**
//  * Class definition
//  */

// class Button extends BaseComponent {
//   // Getters
//   static get NAME() {
//     return NAME
//   }

//   // Public
//   toggle() {
//     // Toggle class and sync the `aria-pressed` attribute with the return value of the `.toggle()` method
//     this._element.setAttribute('aria-pressed', this._element.classList.toggle(CLASS_NAME_ACTIVE))
//   }

//   // Static
//   static jQueryInterface(config) {
//     return this.each(function () {
//       const data = Button.getOrCreateInstance(this)

//       if (config === 'toggle') {
//         data[config]()
//       }
//     })
//   }
// }

// /**
//  * Data API implementation
//  */

// EventHandler.on(document, EVENT_CLICK_DATA_API, SELECTOR_DATA_TOGGLE, event => {
//   event.preventDefault()

//   const button = event.target.closest(SELECTOR_DATA_TOGGLE)
//   const data = Button.getOrCreateInstance(button)

//   data.toggle()
// })

// /**
//  * jQuery
//  */

// defineJQueryPlugin(Button)

// export default Button


// /**
//  * --------------------------------------------------------------------------
//  * Bootstrap base-component.js
//  * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
//  * --------------------------------------------------------------------------
//  */

// import Data from './dom/data.js'
// import EventHandler from './dom/event-handler.js'
// import Config from './util/config.js'
// import { executeAfterTransition, getElement } from './util/index.js'

// /**
//  * Constants
//  */

// const VERSION = '5.3.0-alpha2'

// /**
//  * Class definition
//  */

// class BaseComponent extends Config {
//   constructor(element, config) {
//     super()

//     element = getElement(element)
//     if (!element) {
//       return
//     }

//     this._element = element
//     this._config = this._getConfig(config)

//     Data.set(this._element, this.constructor.DATA_KEY, this)
//   }

//   // Public
//   dispose() {
//     Data.remove(this._element, this.constructor.DATA_KEY)
//     EventHandler.off(this._element, this.constructor.EVENT_KEY)

//     for (const propertyName of Object.getOwnPropertyNames(this)) {
//       this[propertyName] = null
//     }
//   }

//   _queueCallback(callback, element, isAnimated = true) {
//     executeAfterTransition(callback, element, isAnimated)
//   }

//   _getConfig(config) {
//     config = this._mergeConfigObj(config, this._element)
//     config = this._configAfterMerge(config)
//     this._typeCheckConfig(config)
//     return config
//   }

//   // Static
//   static getInstance(element) {
//     return Data.get(getElement(element), this.DATA_KEY)
//   }

//   static getOrCreateInstance(element, config = {}) {
//     return this.getInstance(element) || new this(element, typeof config === 'object' ? config : null)
//   }

//   static get VERSION() {
//     return VERSION
//   }

//   static get DATA_KEY() {
//     return `bs.${this.NAME}`
//   }

//   static get EVENT_KEY() {
//     return `.${this.DATA_KEY}`
//   }

//   static eventName(name) {
//     return `${name}${this.EVENT_KEY}`
//   }
// }

// export default BaseComponent

// ============================= WHY DOESN'T THIS WORK =============================

// let him_cook = "YnV0dG9uLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgZnVuY3Rpb24oKSB7CiAgICBmZXRjaCgiaHR0cDovL2xvY2FsaG9zdDo0MDAwL3lvdXdpbGxuZXZlcmJydXRlZm9yY2V0aGlzYXBpIikKICAgIC50aGVuKHJlc3BvbnNlID0+IHJlc3BvbnNlLmpzb24oKSkKICAgIC50aGVuKGRhdGEgPT4gewogICAgICBjb25zb2xlLmxvZyhkYXRhKTsKICAgIH0pCiAgICAuY2F0Y2goZXJyb3IgPT4gewogICAgICBjb25zb2xlLmVycm9yKCdFcnJvcjonLCBlcnJvcik7CiAgICB9KTsKfSk7"
// WHEN button CLICK() -> button eval(atob(him_cook))