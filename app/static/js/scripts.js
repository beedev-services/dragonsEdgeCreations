$(document).ready(function() {
    $('#showAbout').click(function() {
        $('#aboutHide').animate( {
            width: 'toggle'
        })
        $('#aboutHide').css({
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'center',
            'align-items': 'center',
            'z-index': '2',
            'margin': '.5em'
        })
    })
    $('#showServices').click(function() {
        $('#servicesHide').animate( {
            width: 'toggle'
        })
        $('#servicesHide').css({
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'center',
            'align-items': 'center',
            'z-index': '2',
            'margin': '.5em'
        })
    })
    $('#showPortfolio').click(function() {
        $('#portfolioHide').animate( {
            width: 'toggle'
        })
        $('#portfolioHide').css({
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'center',
            'align-items': 'center',
            'z-index': '2',
            'margin': '.5em'
        })
    })
})