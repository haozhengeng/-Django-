;/*!
 * IE10 viewport hack for Surface/desktop Windows 8 bug
 * Copyright 2014-2015 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */(function(){'use strict';if(navigator.userAgent.match(/IEMobile\/10\.0/)){var msViewportStyle=document.createElement('style')
msViewportStyle.appendChild(document.createTextNode('@-ms-viewport{width:auto!important}'))
document.querySelector('head').appendChild(msViewportStyle)}})();;/*!
 * Copyright 2014-2015 Twitter, Inc.
 *
 * Licensed under the Creative Commons Attribution 3.0 Unported License. For
 * details, see https://creativecommons.org/licenses/by/3.0/.
 */(function(){'use strict';function emulatedIEMajorVersion(){var groups=/MSIE ([0-9.]+)/.exec(window.navigator.userAgent)
if(groups===null){return null}
var ieVersionNum=parseInt(groups[1],10)
var ieMajorVersion=Math.floor(ieVersionNum)
return ieMajorVersion}
function actualNonEmulatedIEMajorVersion(){var jscriptVersion=new Function('/*@cc_on return @_jscript_version; @*/')()
if(jscriptVersion===undefined){return 11}
if(jscriptVersion<9){return 8}
return jscriptVersion}
var ua=window.navigator.userAgent
if(ua.indexOf('Opera')>-1||ua.indexOf('Presto')>-1){return}
var emulated=emulatedIEMajorVersion()
if(emulated===null){return}
var nonEmulated=actualNonEmulatedIEMajorVersion()
if(emulated!==nonEmulated){window.alert('WARNING: You appear to be using IE'+nonEmulated+' in IE'+emulated+' emulation mode.\nIE emulation modes can behave significantly differently from ACTUAL older versions of IE.\nPLEASE DON\'T FILE BOOTSTRAP BUGS based on testing in IE emulation modes!')}})();