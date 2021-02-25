;
	        cm.moveH(-increment, 'char');
	        motionArgs.inclusive = forward ? true : false;
	        var curEnd = moveToCharacter(cm, repeat, forward, lastSearch.selectedCharacter);
	        if (!curEnd) {
	          cm.moveH(increment, 'char');
	          return head;
	        }
	        curEnd.ch += increment;
	        return curEnd;
	      }
	    };

	    function defineMotion(name, fn) {
	      motions[name] = fn;
	    }

	    function fillArray(val, times) {
	      var arr = [];
	      for (var i = 0; i < times; i++) {
	        arr.push(val);
	      }
	      return arr;
	    }
	    /**
	     * An operator acts on a text selection. It receives the list of selections
	     * as input. The corresponding CodeMirror selection is guaranteed to
	    * match the input selection.
	     */
	    var operators = {
	      change: function(cm, args, ranges) {
	        var finalHead, text;
	        var vim = cm.state.vim;
	        vimGlobalState.macroModeState.lastInsertModeChanges.inVisualBlock = vim.visualBlock;
	        if (!vim.visualMode) {
	          var anchor = ranges[0].anchor,
	              head = ranges[0].head;
	          text 