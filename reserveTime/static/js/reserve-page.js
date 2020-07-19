count = 0
$('.menu-items-style').click(function(){
    $('.choosen-items-container').css('display', 'block')
    
    if($(this).data('clicked')) {
        $(this).css('border', '1px solid #ccc')
        $(this).siblings('.menu-item-choose').css('display','none')
        $(this).data('clicked', false);
        if($(this).data('clicked', false)){
            menu_list_classes = $(this).attr('class').split(' ')[$(this).attr('class').split(' ').length -1]
            $(`.choosen-item.${menu_list_classes}`).remove()
            
        }
    }
    else {
        count += 1
        
       $(this).data('clicked', true);
       $(this).css('border', '2px solid #42FF00')
       $(this).siblings('.menu-item-choose').css('display','block')
       $(this).addClass(`item${count}`)
       choosen_item = $('<div></div>') 
       choosen_item.addClass(`row choosen-item item${count}`)
    //    field_number = $('<div class="col-lg-4"></div>')
       meal_count = $('<div class="col-lg-8"></div>')
       decrease = $('<div><button type="button" class="decrease-btn"><i class="fas fa-minus-circle"></i></button></div>')
       decrease.addClass('decrease')
       menu_item_name = $('<div></div>')
       menu_item_name.addClass('menu-item-name')
       menu_item_name.text($(this).find('.menu-title-get').text())
       increase = $('<div><button type="button" class="increase-btn"><i class="fas fa-plus-circle"></i></button></div>')
       increase.addClass('increase')
        meal_count.append(decrease,menu_item_name,increase)
       price = $('<div class="col-lg-4 float-right price"></div>')
       price_span = $('<span class="price-span">1</span>')
       price.append(price_span)
       price_span.text($(this).find('.menu-price-get span').text())
    //    field_number.addClass('field-number')
    //    field_number.text(count)
       meal_count.addClass('meal-count')

       choosen_item.append(meal_count, price)
       
       $('.choosen-items-container').append(choosen_item)
       $('.decrease-btn').prop('disabled', true)
        $('.decrease-btn').animate({opacity: 0.6}, 200)
       if($(".choosen-items-container").is(':empty')){
        console.log('pk')
        $('.choosen-items-container').css('display', 'none')
    }
    }
    plus_count = 1
    meal_pp = $(this).find('.menu-price-get span').text().substring(1, $(this).find('.menu-price-get span').text().length)
    $('.fa-plus-circle').click(function(){
        plus_count += 1
        // console.log(plus_count)
        if(plus_count>1){
            $(this).parents('.increase').siblings('.decrease').children('.decrease-btn').prop('disabled', false)
            $(this).parents('.increase').siblings('.decrease').children('.decrease-btn').animate({opacity: 1}, 200)
        }
        // meal_price = $(this).parents('.mealx -count').siblings('.price').children().text()
        // meal_p = parseFloat(meal_price.substring(1, meal_price.length))
        $(this).parents('.meal-count').siblings('.price').children().text(`$${meal_pp*plus_count}`)
       
        
    })
    $('.decrease-btn').click(function(){
        
        plus_count -= 1
        if(plus_count==1){
            $(this).prop('disabled', true)
            $(this).animate({opacity: 0.6}, 200)
        }
        console.log(plus_count) 
       
        $(this).parents('.meal-count').siblings('.price').children().text(`$${meal_pp * plus_count}`)
        

    })
  })

  $('.table-images').click(function(){
      $('.table-images').animate({opacity: 1}, 200)
      $(this).animate({opacity: 0.6}, 200)
  })
