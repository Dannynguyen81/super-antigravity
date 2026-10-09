(function () {
  "use strict";

  var I18N = window.SAG_I18N || { defaultLang: "vi", meta: {}, strings: {} };
  var STORE_KEY = "sag-lang";

  function supported(lang) {
    return Object.prototype.hasOwnProperty.call(I18N.meta, lang);
  }

  function readStored() {
    try {
      return window.localStorage.getItem(STORE_KEY);
    } catch (e) {
      return null;
    }
  }

  function writeStored(lang) {
    try {
      window.localStorage.setItem(STORE_KEY, lang);
    } catch (e) {
      /* lưu trữ bị chặn: bỏ qua, trang vẫn hoạt động */
    }
  }

  // Mặc định tiếng Việt; chỉ đổi khi người dùng chọn (?lang= hoặc nút chuyển).
  function initialLang() {
    var fromQuery = new URLSearchParams(window.location.search).get("lang");
    if (fromQuery && supported(fromQuery)) return fromQuery;
    var stored = readStored();
    if (stored && supported(stored)) return stored;
    return I18N.defaultLang;
  }

  function translate(key, lang) {
    var entry = I18N.strings[key];
    if (!entry) return null;
    return entry[lang] != null ? entry[lang] : entry[I18N.defaultLang];
  }

  function apply(lang) {
    var meta = I18N.meta[lang];
    document.documentElement.lang = meta.htmlLang;

    document.querySelectorAll("[data-i18n]").forEach(function (node) {
      var value = translate(node.getAttribute("data-i18n"), lang);
      if (value != null) node.textContent = value;
    });

    document.querySelectorAll("[data-i18n-attr]").forEach(function (node) {
      node.getAttribute("data-i18n-attr").split(",").forEach(function (pair) {
        var parts = pair.split(":");
        var value = translate(parts[1], lang);
        if (value != null) node.setAttribute(parts[0], value);
      });
    });

    var title = translate("meta.title", lang);
    if (title) document.title = title;

    document.querySelectorAll("[data-lang-current]").forEach(function (node) {
      node.textContent = meta.short;
    });
    document.querySelectorAll("[data-lang]").forEach(function (btn) {
      btn.parentNode.setAttribute("aria-selected", String(btn.getAttribute("data-lang") === lang));
    });
  }

  function setLang(lang) {
    if (!supported(lang)) return;
    apply(lang);
    writeStored(lang);
  }

  function initMenu() {
    var root = document.querySelector("[data-lang-switch]");
    if (!root) return;
    var button = root.querySelector(".langswitch__button");
    var menu = root.querySelector(".langswitch__menu");

    function close() {
      menu.hidden = true;
      button.setAttribute("aria-expanded", "false");
    }

    button.addEventListener("click", function () {
      var open = menu.hidden;
      menu.hidden = !open;
      button.setAttribute("aria-expanded", String(open));
    });
    menu.addEventListener("click", function (event) {
      var target = event.target.closest("[data-lang]");
      if (!target) return;
      setLang(target.getAttribute("data-lang"));
      close();
      button.focus();
    });
    document.addEventListener("click", function (event) {
      if (!root.contains(event.target)) close();
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") close();
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    apply(initialLang());
    initMenu();
  });
})();
