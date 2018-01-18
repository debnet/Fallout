
// Gestion des onglets
$('.tab a').click(function(event) {
    event.preventDefault();
    $(this).tab('show');
});

// (Dés)activation des contrôles ciblés par des cases à cocher
$('input[type=checkbox]').click(function(event) {
    var input = $('#' + $(this).data('target'));
    var checked = $(this).is(':checked');
    input.prop('disabled', !checked);
});

$('a[data-toggle="tab"]').on('shown.bs.tab', function(event) {
   localStorage.activePanel = event.target.id;
});

// Affichage du premier onglet par défaut
if ($('.tab-pane.active').length === 0) {
    var activePanel = $('#' + localStorage.activePanel);
    if (activePanel.length) {
        activePanel.click();
    } else {
        $('.tab a:first').click();
    }
}

// Fonction de transformation des données pour l'autocomplétion
function transformData(data, label, value, other) {
    label = label || 'name';
    value = value || 'id';
    var result = [];
    data['results'].forEach(function(e) {
        result.push({
            value: e[label] + (other ? ' (' + e[other] + ')' : ''),
            id: e[value]
        })
    });
    return result;
}

// Autocomplétion des objets
$('#item-name').autocomplete({
    source: function(request, response) {
        $.ajax({
            url: "/api/fallout/item/",
            data: {
                name__icontains: request.term,
                fields: 'id,name,type',
                order_by: 'name',
                display: '1'
            },
            success: function(data) {
                response(transformData(data, 'name', 'id', 'type_display'));
            }
        });
    },
    minLength: 2,
    select: function(event, ui) {
        $('#' + $(this).data('for')).val(ui.item.id);
    }
}).focus(function() {
    $(this).select();
});

// Autocomplétion des effets
$('#effect-name').autocomplete({
    source: function(request, response) {
        $.ajax({
            url: "/api/fallout/effect/",
            data: {
                name__icontains: request.term,
                fields: 'id,name',
                order_by: 'name'
            },
            success: function(data) {
                response(transformData(data));
            }
        });
    },
    minLength: 2,
    select: function(event, ui) {
        $('#' + $(this).data('for')).val(ui.item.id);
    }
}).focus(function() {
    $(this).select();
});

// Autocomplétion des butins
$('#loot-name').autocomplete({
    source: function(request, response) {
        $.ajax({
            url: "/api/fallout/loottemplate/",
            data: {
                name__icontains: request.term,
                fields: 'id,name',
                order_by: 'name'
            },
            success: function(data) {
                response(transformData(data));
            }
        });
    },
    minLength: 2,
    select: function(event, ui) {
        $('#' + $(this).data('for')).val(ui.item.id);
    }
}).focus(function() {
    $(this).select();
});


// Jets de dés
var diceRoller = new DiceRoller();
function roll() {
    var value = $('#diceroll-input').val();
    var roll = diceRoller.roll(value);
    $('#diceroll-output').val(roll.getNotation());
    return false;
}

$('#diceroll').on('shown.bs.modal', function () {
    $('#diceroll-input').trigger('focus').select();
});

$.key('ctrl+b', function() {
    $('#diceroll').modal();
});
