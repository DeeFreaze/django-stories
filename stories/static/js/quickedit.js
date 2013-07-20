// Generated by CoffeeScript 1.3.1
(function() {

  (function($) {
    var updateSel;
    updateSel = function(elem, selector) {
      var selId;
      selId = $(elem).attr('id');
      return $("" + selector + " #" + selId).val($(elem).val());
    };
    return $(document).ready(function() {
      $('.quickedit').each(function() {
        return $(this).click(function() {
          var id, target;
          id = $(this).attr('id').replace('quickedit-', '');
          target = $("#qe-form-" + id);
          $(target).toggle();
          return $('.qe-reset', target).click(function() {
            return $(target).toggle();
          });
        });
      });
      $('#result_list select').change(function() {
        updateSel(this, '.quickedit-row');
        return $(this).parent().parent().css('background', '#FFC');
      });
      return $('.quickedit-row select').change(function() {
        return updateSel(this, '#result_list');
      });
    });
  })(django.jQuery);

}).call(this);