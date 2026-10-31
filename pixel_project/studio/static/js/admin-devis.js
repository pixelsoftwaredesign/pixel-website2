/* Éditeur de lignes (devis / préfactures). Aucune dépendance externe. */
(function () {
  'use strict';

  function nombre(valeur) {
    var n = parseFloat(String(valeur || '').replace(',', '.'));
    return isNaN(n) ? 0 : n;
  }

  function init(config) {
    var tbody = document.getElementById(config.tableId);
    var template = document.getElementById(config.templateId);
    var totalInput = document.querySelector(
      '[name="' + config.totalFormsName + '"]');
    var dataNode = document.getElementById(config.productsDataId);
    if (!tbody || !template || !totalInput || !dataNode) return;

    var produits = {};
    try { produits = JSON.parse(dataNode.textContent || '{}'); } catch (e) {}

    function recalc() {
      var totalHt = 0;
      tbody.querySelectorAll('tr[data-line]').forEach(function (row) {
        var suppr = row.querySelector('input[type="checkbox"][name$="-DELETE"]');
        var qte = row.querySelector('[data-quantite]');
        var prix = row.querySelector('[data-prix]');
        var remise = row.querySelector('[data-remise]');
        var cell = row.querySelector('.line-total');
        if (!qte || !prix) return;
        var total = 0;
        if (!suppr || !suppr.checked) {
          total = nombre(qte.value) * nombre(prix.value) *
            (1 - nombre(remise && remise.value) / 100);
        }
        totalHt += total;
        if (cell) cell.textContent = total.toFixed(2);
      });
      var tva = nombre((document.getElementById(config.tvaId) || {}).value);
      var ht = document.getElementById(config.totalHtId);
      var ttc = document.getElementById(config.totalTtcId);
      if (ht) ht.textContent = totalHt.toFixed(2);
      if (ttc) ttc.textContent = (totalHt * (1 + tva / 100)).toFixed(2);
    }

    function ajouterLigne(produitId) {
      var index = parseInt(totalInput.value, 10) || 0;
      var html = template.innerHTML.replace(/__prefix__/g, index);
      var wrapper = document.createElement('tbody');
      wrapper.innerHTML = html;
      var row = wrapper.querySelector('tr');
      if (!row) return;
      tbody.appendChild(row);
      totalInput.value = index + 1;
      if (produitId) {
        var select = row.querySelector('[data-produit-select]');
        if (select) {
          select.value = String(produitId);
          select.dispatchEvent(new Event('change', {bubbles: true}));
        }
      }
      var first = row.querySelector('[data-quantite]');
      if (first && !produitId) first.focus();
      recalc();
    }

    var addButton = document.getElementById(config.addButtonId);
    if (addButton) addButton.addEventListener('click', function () {
      ajouterLigne(null);
    });

    tbody.addEventListener('change', function (event) {
      var select = event.target.closest('[data-produit-select]');
      if (select) {
        var row = select.closest('tr');
        var produit = produits[select.value];
        if (produit && row) {
          var designation = row.querySelector('[data-designation]');
          var prix = row.querySelector('[data-prix]');
          if (designation) designation.value = produit.nom;
          if (prix) prix.value = produit.prix;
        }
      }
      recalc();
    });
    tbody.addEventListener('input', function (event) {
      if (event.target.matches(
          '[data-quantite], [data-prix], [data-remise]')) recalc();
    });

    document.querySelectorAll(config.catalogueSelector).forEach(function (btn) {
      btn.addEventListener('click', function () {
        ajouterLigne(btn.getAttribute('data-produit-id'));
      });
    });

    var filtre = document.getElementById(config.filterId);
    if (filtre) {
      filtre.addEventListener('input', function () {
        var terme = filtre.value.trim().toLowerCase();
        document.querySelectorAll(config.catalogueSelector).forEach(function (btn) {
          var texte = (btn.getAttribute('data-search') || '').toLowerCase();
          btn.hidden = Boolean(terme) && texte.indexOf(terme) === -1;
        });
      });
    }

    recalc();
  }

  window.PixelLineEditor = {init: init};
})();
