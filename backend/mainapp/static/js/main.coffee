(($) ->

  MD_MAX_WIDTH = 991
  SM_MAX_WIDTH = 767

  window.addEventListener("orientationchange", ->
    refreshGrid()
  , false)

  window.addEventListener("resize", ->
    refreshGrid()
  , false)

  refreshGrid = ->
    # prevent closing sidebar on mobile when scrolling
    cachedWidth = $(window).width()
    $(window).resize ->
        newWidth = $(window).width()
        if newWidth != cachedWidth && newWidth < 767
          cachedWidth = newWidth
          sidebarClose()
          sidebarDom.clearQueue() # stop aniamtions


  sidebarDom = $ '#sidebar-wrapper'
  contentWrapper = $ '#content-wrapper'

  navbarCloseBtn = $ '#navbar-sidebar-close'
  navbarOpenBtn = $ '#navbar-sidebar-open'

  sidebarClose = ->
    sidebarDom.animate({marginLeft: '-83%' }, '100', ->
      sidebarDom.removeAttr 'style'
    )
    sidebarDom.addClass('sidebar-closed')
    navbarCloseBtn.addClass('d-none')
    navbarOpenBtn.removeClass('d-none')

    # we dont need closing sidebar
    contentWrapper.off('click')

  sidebarOpen = ->
    sidebarDom.animate({marginLeft: '0px'}, '250', ->
      sidebarDom.removeAttr 'style'
    )

    $("html, body").animate({ scrollTop: 0 }, 600); # scroll top when menu open
    sidebarDom.removeClass('sidebar-closed')

    navbarOpenBtn.addClass('d-none')
    navbarCloseBtn.removeClass('d-none')

    #hide sidebar when click on content
    contentWrapper.click (e) ->
      sidebarClose()
      e.stopPropagation()




  $('#navbar-sidebar-close, #sidebar-overlay').on 'click', ->
    sidebarClose()

  $('#navbar-sidebar-open').on 'click', ->
    sidebarOpen()


  # Clickable row
  $('.clickable-row').click ->
    window.location = $(this).data('href')





) jQuery