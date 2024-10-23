import sys
import time
import shutil
import threading
import itertools
from datetime import datetime

class Loading:
    def __init__(self, message=None, style='classic'):
        try:
            self.default_messages = {
                'chat': 'Assistant is thinking...',
                'vision': 'Analyzing image...',
                'default': 'Processing request...'
            }

            self.spinner_styles = {
                'classic': ['|', '/', '-', '\\'],
                'dots': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
            }

            self.style = style
            self.running = False
            self._thread = None
            self.start_time = None
            self._lock = threading.Lock()
            self.is_streaming = False
            
            try:
                self.bar_width = min(shutil.get_terminal_size().columns - 30, 50)
            except:
                raise Exception("Failed to get terminal size")
            
            self.bar_format = '█'
            self.bar_empty = '░'
            
            self.message = message or self.default_messages['chat']
            self.spinner = self.spinner_styles[style]
            
            self.progress = 0
            self.total_progress = 0
            self.show_time = True
            
        except Exception as e:
            raise Exception(f"Failed to initialize loading indicator: {str(e)}")

    def start(self, operation_type=None, message=None, style=None, streaming=False):
        try:
            if style:
                self.set_style(style)
            if message or operation_type:
                self.set_message(operation_type, message)
                
            with self._lock:
                if not self.running:
                    self.running = True
                    self.is_streaming = streaming
                    self.start_time = datetime.now()
                    if not streaming:
                        self._thread = threading.Thread(target=self._animate)
                        self._thread.daemon = True
                        self._thread.start()
            return self
            
        except Exception as e:
            raise Exception(f"Failed to start loading animation: {str(e)}")

    def stop(self):
        try:
            with self._lock:
                if self.running:
                    self.running = False
                    if self._thread:
                        self._thread.join()
                    if not self.is_streaming:
                        self._clear_line()
                        
        except Exception as e:
            raise Exception(f"Failed to stop loading animation: {str(e)}")

    def _animate(self):
        try:
            spinner_cycle = itertools.cycle(self.spinner)
            dots_cycle = itertools.cycle(['   ', '.  ', '.. ', '...'])
            
            while self.running and not self.is_streaming:
                try:
                    if self.total_progress > 0:
                        self._draw_progress_bar()
                    else:
                        self._draw_spinner(next(spinner_cycle), next(dots_cycle))
                    time.sleep(0.1)
                except Exception:
                    time.sleep(0.1)
                    continue
                    
        except Exception as e:
            self.running = False
            raise Exception(f"Animation loop failed: {str(e)}")

    def set_message(self, operation_type=None, custom_message=None):
        try:
            with self._lock:
                if custom_message:
                    if not isinstance(custom_message, str):
                        raise Exception("Custom message must be a string")
                    self.message = custom_message
                elif operation_type in self.default_messages:
                    self.message = self.default_messages[operation_type]
                else:
                    raise Exception(f"Invalid operation type. Must be one of: {', '.join(self.default_messages.keys())}")
            return self
        except Exception as e:
            raise Exception(f"Failed to set message: {str(e)}")

    def set_style(self, style):
        try:
            if style not in self.spinner_styles:
                raise Exception(f"Invalid spinner style. Must be one of: {', '.join(self.spinner_styles.keys())}")
                
            with self._lock:
                self.spinner = self.spinner_styles[style]
                self.style = style
                
            return self
            
        except Exception as e:
            raise Exception(f"Failed to set style: {str(e)}")

    def set_progress(self, current, total):
        try:
            if not isinstance(current, (int, float)) or not isinstance(total, (int, float)):
                raise Exception("Progress values must be numbers")
            if current < 0 or total < 0:
                raise Exception("Progress values cannot be negative")
            if current > total:
                raise Exception("Current progress cannot exceed total")
            
            with self._lock:
                self.progress = current
                self.total_progress = total
                
            return self
            
        except Exception as e:
            raise Exception(f"Failed to set progress: {str(e)}")

    def _draw_spinner(self, spinner_char, dots):
        try:
            with self._lock:
                elapsed = datetime.now() - self.start_time if self.start_time else datetime.now()
                elapsed_str = str(elapsed).split('.')[0] if self.show_time else ''
                
                message = f'\r{spinner_char} {self.message}{dots}'
                if self.show_time:
                    message += f' ({elapsed_str})'
                
                try:
                    term_width = shutil.get_terminal_size().columns
                except (AttributeError, OSError):
                    term_width = 80
                    
                if len(message) > term_width:
                    message = message[:term_width-3] + '...'
                    
                sys.stdout.write(message)
                sys.stdout.flush()
                
        except Exception as e:
            raise Exception(f"Failed to draw spinner: {str(e)}")

    def _draw_progress_bar(self):
        try:
            with self._lock:
                percentage = min(100, round(self.progress / self.total_progress * 100))
                filled_length = int(self.bar_width * percentage // 100)
                
                bar = (
                    self.bar_format * filled_length +
                    self.bar_empty * (self.bar_width - filled_length)
                )
                
                elapsed = datetime.now() - self.start_time if self.start_time else datetime.now()
                elapsed_str = str(elapsed).split('.')[0] if self.show_time else ''
                
                line = f'\r{self.message} [{bar}] {percentage}%'
                if self.show_time:
                    line += f' ({elapsed_str})'
                    
                try:
                    term_width = shutil.get_terminal_size().columns
                except (AttributeError, OSError):
                    term_width = 80
                    
                if len(line) > term_width:
                    line = line[:term_width-3] + '...'
                    
                sys.stdout.write(line)
                sys.stdout.flush()
                
        except Exception as e:
            raise Exception(f"Failed to draw progress bar: {str(e)}")

    def update_progress(self, current, total, message=None):
        try:
            self.set_progress(current, total)
            if message:
                self.set_message(custom_message=message)
            return self
        except Exception as e:
            raise Exception(f"Failed to update progress: {str(e)}")

    def pulse(self, message=None):
        try:
            if message:
                if not isinstance(message, str):
                    raise Exception("Pulse message must be a string")
                self.message = message
            
            chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
            for char in chars:
                sys.stdout.write(f'\r{char} {self.message}')
                sys.stdout.flush()
                time.sleep(0.05)
            
            self._clear_line()
            
        except Exception as e:
            raise Exception(f"Failed to show pulse animation: {str(e)}")

    def _clear_line(self):
        try:
            try:
                columns = shutil.get_terminal_size().columns
            except (AttributeError, OSError):
                columns = 80
                
            sys.stdout.write('\r' + ' ' * (columns - 1) + '\r')
            sys.stdout.flush()
            
        except Exception as e:
            raise Exception(f"Failed to clear terminal line: {str(e)}")