gulp = require('gulp')

clean = require('gulp-clean')
coffee = require('gulp-coffee')
coffeelint = require('gulp-coffeelint')
gutil = require('gulp-util')
less = require('gulp-less')
recess = require('gulp-recess')
uglify = require('gulp-uglify')
uglifycss = require('gulp-uglifycss')
runSequence = require('run-sequence')

jsDir = '*/static/**/*.js'
coffeeDir = '*/static/**/*.coffee'
cssDir = '*/static/**/*.css'
lessDir = '*/static/**/*.less'

# Clean old JS
gulp.task 'clean-js', ->
  return gulp.src(jsDir, read: false)
    .pipe(clean())

# Lint Coffeescript
gulp.task 'lint-coffee', ->
  return gulp.src(coffeeDir)
    .pipe(coffeelint())
    .pipe(coffeelint.reporter('default'))

# Convert Coffeescript to JS
gulp.task 'coffee-to-js', ->
  return gulp.src(coffeeDir)
    .pipe(coffee(bare: true).on('error', gutil.log))
    .pipe(gulp.dest('.'))

# Minify JS
gulp.task 'minify-js', ->
  return gulp.src(jsDir)
    .pipe(uglify())
    .pipe(gulp.dest('.'))

# Clean CSS
gulp.task 'clean-css', ->
  return gulp.src(cssDir, read: false)
    .pipe(clean())

# Lint Less
gulp.task 'lint-less', ->
  return gulp.src(lessDir)
    .pipe(recess())
    .pipe(recess.reporter())

# Compile Less to CSS
gulp.task 'less-to-css', ->
  return gulp.src(lessDir)
    .pipe(less())
    .pipe(gulp.dest('.'))


# Minify CSS
gulp.task 'minify-css', ->
  return gulp.src(cssDir)
    .pipe(uglifycss())
    .pipe(gulp.dest('.'))

# Build coffee
gulp.task 'coffee-build', ->
  runSequence('clean-js', 'lint-coffee', 'coffee-to-js', 'minify-js')

# Build css
gulp.task 'less-build', ->
  runSequence('clean-css', 'lint-less', 'less-to-css', 'minify-css')

# Watch Files For Changes
gulp.task 'watch', ->
  gulp.watch coffeeDir, ['coffee-build']
  gulp.watch lessDir, ['less-build']

# Build coffee and css
gulp.task 'both-build', ['coffee-build', 'less-build']

# Default Task
gulp.task 'default', ->
  runSequence('both-build', 'watch')
